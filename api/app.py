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


@app.route("/query", methods=["GET"])
def test_query_return():
    q = request.args.get('q')
    return process_query(q)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
