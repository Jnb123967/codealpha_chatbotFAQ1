from flask import Flask, request, jsonify
import json
import difflib

app = Flask(__name__)

with open("faq_data.json", "r") as file:
    faqs = json.load(file)

def find_best_answer(user_question):
    questions = [faq["question"] for faq in faqs]
    match = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.5)
    if match:
        for faq in faqs:
            if faq["question"] == match[0]:
                return faq["answer"]
    return "Sorry, I don't know the answer to that question."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    answer = find_best_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)