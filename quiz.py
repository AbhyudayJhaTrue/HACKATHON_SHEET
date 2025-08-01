from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def quiz():
    url = "https://opentdb.com/api.php?amount=5&category=17&type=multiple"
    response = requests.get(url)
    questions = response.json()["results"]

    formatted_questions = []
    for q in questions:
        all_answers = q["incorrect_answers"] + [q["correct_answer"]]
        random.shuffle(all_answers)
        formatted_questions.append({
            "question": q["question"],
            "answers": all_answers,
            "correct": q["correct_answer"]
        })

    return render_template("index.html", questions=formatted_questions)

if __name__ == "__main__":
    app.run(debug=True)
