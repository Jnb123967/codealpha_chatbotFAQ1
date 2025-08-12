# FAQ Chatbot (Flask)

A small FAQ chatbot that uses TF‑IDF + cosine similarity to match user questions to stored FAQs.

## Files
- `app.py` — Flask web app (serves UI and `/api/ask` endpoint)
- `faq_bot.py` — simple TF‑IDF matching engine
- `faqs.json` — sample FAQ data (edit to add your own)
- `templates/index.html` — web UI
- `requirements.txt` — Python dependencies

## Quick start (local)
1. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # (on Windows use `venv\Scripts\activate`)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser at `http://127.0.0.1:5000` and try the chat UI.

## Notes
- If you prefer not to install `scikit-learn`, you can replace the matching code in `faq_bot.py` with a simple substring or difflib-based matcher.
- To add FAQs, edit `faqs.json` — it's an array of objects with `question` and `answer` fields.
