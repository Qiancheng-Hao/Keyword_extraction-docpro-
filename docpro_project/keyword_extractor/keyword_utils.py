# keyword_extractor/keyword_utils.py
import yake

def extract_keywords(text, num_keywords=10):
    kw_extractor = yake.KeywordExtractor(n=2, top=num_keywords)
    keywords = kw_extractor.extract_keywords(text)
    return [kw[0] for kw in keywords]
