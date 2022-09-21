from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen
if __name__ == "__main__":
    try:
        from gevent.pywsgi import WSGIServer
        http_server = WSGIServer(("", 80), app,log = None)
        http_server.serve_forever()
    except Exception as e:
        print(e)
        app.run(host="0.0.0.0", port=80)