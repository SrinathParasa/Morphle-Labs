from flask import Flask
import os
from datetime import datetime
import subprocess
import platform
import pwd

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Srinath Parasa"
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    
    # Intially, I wrote code for my windows system
    # Then updated it to handle both windows and Linux/Unix(github codespaces)

    if platform.system() == "Windows":
        # Windows-specific username and task list
        try:
            username = os.getlogin()
            top_output = subprocess.check_output("tasklist", shell=True).decode("utf-8")
        except Exception:
            username = "Unknown User"
            top_output = "Could not retrieve task list."
    else:
        # Linux-specific username and top output (GitHub Codespaces)
        try:
            username = os.getenv("USER") or pwd.getpwuid(os.getuid()).pw_name
            top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
        except Exception:
            username = "Unknown User"
            top_output = "Could not retrieve top output."

    return f"<h1>Name: {name}</h1><h2>Username: {username}</h2><h3>Server Time: {server_time}</h3><pre>{top_output}</pre>"

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)