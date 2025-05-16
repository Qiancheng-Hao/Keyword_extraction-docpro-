# Keyword_extraction-docpro

curl -X POST http://127.0.0.1:8000/api/extract_keywords/ -H "Content-Type: application/json" -d '{"text": "Artificial intelligence is a wonderful field that combines computer science and statistics to create intelligent systems.", "num_keywords": 5}'

python cli.py --text "Artificial intelligence is a wonderful field that combines computer science and statistics to create intelligent systems." --num 5
