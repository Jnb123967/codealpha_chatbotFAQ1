from flask import Flask, request, jsonify, render_template
from faq_bot import FAQBot
import os

app = Flask(__name__)
# instantiate chatbot; it will load faqs.json from project root
bot = FAQBot(faq_path=os.path.join(app.root_path, 'faqs.json'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json(force=True)
    q = data.get('question', '')
    result = bot.answer(q)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
