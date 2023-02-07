from flask import Flask
from flask.app import Flask as FlaskApp

app = Flask(__name__)

@app.route("/")
def i_knew():
    return "I <b>knew</b> that you`ll come"

if __name__=="__main__":
    app.run(
        port = 8080,
        debug = True
    )