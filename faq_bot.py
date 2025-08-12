import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

class FAQBot:
    def __init__(self, faq_path='faqs.json', min_score=0.35):
        self.faq_path = faq_path
        self.min_score = min_score
        self.faqs = []
        self.questions = []
        self.answers = []
        self.vectorizer = None
        self.tfidf_matrix = None
        self._load_faqs()

    def _load_faqs(self):
        p = self.faq_path
        if not os.path.exists(p):
            raise FileNotFoundError(f"FAQ file not found: {p}")
        with open(p, 'r', encoding='utf-8') as f:
            self.faqs = json.load(f)
        self.questions = [q['question'] for q in self.faqs]
        self.answers = [q['answer'] for q in self.faqs]
        self.vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)

    def answer(self, user_question):
        if not user_question or not user_question.strip():
            return {'answer': "Please enter a question.", 'score': 0.0, 'match': None}
        q_vec = self.vectorizer.transform([user_question])
        # cosine similarity via linear_kernel (fast)
        sims = linear_kernel(q_vec, self.tfidf_matrix).flatten()
        top_idx = np.argmax(sims)
        top_score = float(sims[top_idx])
        if top_score >= self.min_score:
            return {'answer': self.answers[top_idx], 'score': top_score, 'match': self.questions[top_idx]}
        else:
            return {'answer': "Sorry, I don't know the answer to that. Try rephrasing or ask something else.", 'score': top_score, 'match': None}

if __name__ == '__main__':
    bot = FAQBot()
    while True:
        q = input('Ask a question (or "exit"): ').strip()
        if q.lower() in ('exit','quit'):
            break
        r = bot.answer(q)
        print(f"Score: {r['score']:.3f}\nAnswer: {r['answer']}\nMatched: {r.get('match')}")
