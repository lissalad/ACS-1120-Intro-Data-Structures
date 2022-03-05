"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from dictogram import Dictogram
from markov import Markov
from tokens import tokenize

app = Flask(__name__)

words = tokenize('./tmdb_horror.txt')
histogram = Dictogram(words)

markov = Markov(histogram, words)



@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
  


@app.route("/")
def home():
    return render_template("index.html", tweet=markov.sentence(histogram, 20))


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
