# cli.py
import requests
import argparse


def extract_keywords_cli(text, num_keywords=10):
    url = "http://127.0.0.1:8000/api/extract_keywords/"
    payload = {
        "text": text,
        "num_keywords": num_keywords
    }
    response = requests.post(url, json=payload)
    return response.json()


def main():
    parser = argparse.ArgumentParser(description="Extract keywords from text")
    parser.add_argument("--text", type=str, required=True, help="Input text")
    parser.add_argument("--num", type=int, default=10, help="Number of keywords to extract")
    args = parser.parse_args()

    result = extract_keywords_cli(args.text, args.num)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Keywords:")
        for keyword in result["keywords"]:
            print(f"- {keyword}")


if __name__ == "__main__":
    main()