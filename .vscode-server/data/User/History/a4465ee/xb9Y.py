from flask import Flask
app = Flask(__name__)
if __name__ == "_main_":
    host = "127.0.0.1"
    port = 4000
    app.run(host,port)