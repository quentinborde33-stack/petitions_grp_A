from flask import Flask, render_template, send_from_directory

app = Flask("petitions")


@app.get("/")
def index():
    return render_template("index.html", nombre_signatures=1)


@app.get("/style.css")
def sytle():
    return send_from_directory("static", "style.css")
