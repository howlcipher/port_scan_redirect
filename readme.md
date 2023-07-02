<h1>A website redirection based on response code and port open.</h1>

<h2>How to run:</h2>
<p>Run "python flask_app.py" in one terminal and "specific_port.py" in a second terminal.</p>

<h2>Expected Output:</h2>
<ul>
<li>If both terminals are running, 127.0.0.1:1337 will be redirected to 127.0.0.1:5000 in 5 seconds.  The browser will display "Hello World!" and then "Goodbye World!"</li>
<li>If the "flask_app.py" is not running, 127.0.0.1:1337/redirect with occur in 5 seconds and display the site and port that was unable to be redirected to.</li>
</ul>

<h2>Configuration:</h2>
<h3>In specific_port.py</h3>
<ul>
<li>Set target as a site or IP address</li>
<li>Set port as a port number</li>
<ul>