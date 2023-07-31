from flask import Flask

app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return "get request"
    else:
        return "post request"