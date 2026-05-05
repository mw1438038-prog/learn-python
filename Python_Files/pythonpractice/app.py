from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my first app!"

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        message = "Button was clicked!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
