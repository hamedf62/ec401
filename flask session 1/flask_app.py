from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template("app.html")


@app.route("/country/<dest_country>")
def hello_country(dest_country):
    return render_template("country.html", country=dest_country)


if __name__ == "__main__":
    app.run(port=5050,debug=True)