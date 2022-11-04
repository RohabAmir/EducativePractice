"""Rendering HTML Templates for my web pages"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html")


@app.route("/Info")
def about():
    """View function for Info Page."""
    return render_template("info.html")

@app.route("/Contact")
def contact():
    """View function for Contact Page."""
    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
