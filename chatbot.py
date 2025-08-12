import json
import difflib

# Load FAQs from JSON file
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

# Main loop
print("FAQ Chatbot (type 'quit' to exit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    response = find_best_answer(user_input)
    print("Bot:", response)