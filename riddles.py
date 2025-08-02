from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def riddle():
    url = "https://riddles-api-eight.vercel.app/science"
    response = requests.get(url)
    data = response.json()
    riddle = data.get("riddle", "No riddle found.")
    answer = data.get("answer", "No answer found.")
    return render_template("website.html", riddle=riddle, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
