# AI eLearning Path Generator

A prototype I built as part of a university AI consultancy team for a UK client. This repository holds my learning-path prototype only and contains no client data. It's a Flask web app that sends a learner's goal to the OpenAI API and gets back:

- **tags**: the relevant topics
- **path**: a step-by-step learning plan

## Tech stack
- Python / Flask
- OpenAI API
- python-dotenv
- HTML template (Jinja2)

## Run locally
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
cp .env.example .env          # then put your OpenAI key in .env
python API_get_text.py
```
Then open http://localhost:5000
