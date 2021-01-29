<h1> Apartments-Flask_Web_App </h1>

<p>A repository for a school project.</br>
Subject: Software Development.</br>
Project: Flask Web Application.</p>

<h3>Running a flask server in Debug mode:</h3>
<ul>
    <li>export FLASK_APP={router_name}.py</li>
    <li>export FLASK_ENV=development</li>
    <li>export FLASK_DEBUG=1</li>
    <li>python -m flask run</li>
</ul>

<h3>requirements.txt</h3>
<div>This is a file with the required Python modules for installing the project.</br>
They will be automatically installed after running the following command:</div>
<ul>
<li>python3 -m pip install -r requirements.txt</li>
</ul>

<h3>!!! flask_uploads.py from module Flask-Uploads is edited</h3>
<p>Instead of <i>"from werkzeug import secure_filename, FileStorage"</i> we have:</p>
<ul>
    <li>from werkzeug.utils import secure_filename</li>
    <li>from werkzeug.datastructures import FileStorage</li>
</ul>
<p>That fixes a strange ImportError.</p>
