import platform
from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Srinath Parasa"
    username = os.getlogin()
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    try:
        if platform.system() == "Windows":
            # my system is windows so this function call
            top_output = subprocess.check_output("tasklist", shell=True).decode("utf-8")
        else:
            # As GitHub Codespaces run on Linux/Unix, this function call
            top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        top_output = "Could not retrieve task list."

    return f"<h1>Name: {name}</h1><h2>Username: {username}</h2><h3>Server Time: {server_time}</h3><pre>{top_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
