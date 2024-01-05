from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello World!!"


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_username = request.form.get("username")
    input_password = request.form.get("password")
    return render_template(
        "success.html", username=input_username, password=input_password)
