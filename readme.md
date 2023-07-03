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
<li>Common ports: 80 (http), 443 (https)</li>
</ul>

<h2>Build and run as a service:</h2>
<ul>
<li>Use <a href='https://pyinstaller.org/en/stable/usage.html'>pyinstaller</a> and run "pyinstaller --onefile specific_port.py" in the terminal</li>
<ul>
<li>Use a third party tool such as <a href='https://nssm.cc/'>NSSM</a> to install as a service</li>
<li>With NSSM installed run "nssm install &ltservice name&gt</li>
<ul>
<li>When GUI launches - Path: navigate to the pyinstaller created exe file.</li>
<li>Save and run</li>
<li>Navigate to Window's services and start the service</li>
</ul>
</ul>
</ul>