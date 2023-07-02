from flask import Flask, redirect
import socket
import requests


app = Flask(__name__) # running as a flask instance
target = '127.0.0.1'  # IP or domain to switch to
port = 5000  # port to connect to

# Scans the target for a specific port.  If response code is 200 the redirect will happen
def port_scan(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open on {target}")
        redirect_url = f'http://{target}:{port}'
        try:
            response = requests.head(redirect_url)
            if response.status_code == 200:
                print(f"Redirecting traffic to: {redirect_url}")
                return redirect_url
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving headers: {e}")
    else:
        print(f"Port {port} is not open on {target}")

    s.close()
    return None

# gets a response code from the server of the target and port 
def perform_redirection(target, port):
    redirect_url = port_scan(target, port)
    if redirect_url:
        return redirect(redirect_url, code=302)
    return None

# the main route with a delay of 5 seconds before redirecting
@app.route("/")
def main_route():
    # Javascript is used to delay the redirect - eliminate it to have this occur immediately
    return """
    <h1>Hello, World!</h1>
    <script>
        setTimeout(function() {
            window.location.href = "/redirect";
        }, 5000);  // Delay for 5 seconds (in milliseconds)
    </script>
    """

# the route to redirect to
@app.route("/redirect")
def redirect_route():
    redirection_response = perform_redirection(target, port)
    if redirection_response:
        return redirection_response

    # if the redirect is not successful - the target and port are not open
    return f"Redirection failed - Site: {target} and Port: {port}"

if __name__ == "__main__":
    app.run(port=1337, debug=True) # localhost:1337
