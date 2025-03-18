from flask import Flask
import subprocess
import datetime
import os
import getpass

app = Flask(__name__)

def get_top_output():
    result = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True)
    return result.stdout

@app.route("/htop")
def htop():
    name = "hema sai keta"
    username = getpass.getuser()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = get_top_output()

    return f"""
    <html>
    <body>
        <h1>System Info</h1>
        <p><b>Name:</b> {name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)