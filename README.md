# Keyword_extraction-docpro

# POST Request
curl -X POST http://127.0.0.1:8000/api/extract_keywords/ \
-H "Content-Type: application/json" \
-d '{"text": "Your input text", "num_keywords": 5}'

curl -X POST http://127.0.0.1:8000/api/extract_keywords/ -H "Content-Type: application/json" -d '{"text": "Artificial intelligence is a wonderful field that combines computer science and statistics to create intelligent systems.", "num_keywords": 5}'

# Run CLI

python cli.py --text "Your input text" --num 5

e.g. python cli.py --text "Artificial intelligence is a wonderful field that combines computer science and statistics to create intelligent systems." --num 5
