from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def quiz():
    try:
        url = "https://opentdb.com/api.php?amount=5&category=17&type=multiple"
        response = requests.get(url)
        data = response.json()
        
        if "results" not in data:
            # Fallback data if API fails
            questions = [
                {
                    "question": "What is the chemical symbol for water?",
                    "incorrect_answers": ["H2O2", "HO", "H3O"],
                    "correct_answer": "H2O"
                },
                {
                    "question": "What planet is known as the Red Planet?",
                    "incorrect_answers": ["Venus", "Jupiter", "Saturn"],
                    "correct_answer": "Mars"
                }
            ]
        else:
            questions = data["results"]

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
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
