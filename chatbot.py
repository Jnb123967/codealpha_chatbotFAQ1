import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
with open("faq.json", "r") as f:
    faqs = json.load(f)

# Preprocess questions
questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

# Initialize vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    return answers[idx]

if __name__ == "__main__":
    print("FAQ Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", chatbot_response(user_input))
