import spacy

nlp = spacy.load("en_core_web_sm")

def check_compliance(text: str) -> dict:
    doc = nlp(text)
    long_sentences = []
    passive_voice = []
    adverb_overuse = []
    complex_words = []

    for sent in doc.sents:
        if len(sent) > 25:
            long_sentences.append(sent.text)

        for token in sent:
            if token.dep_ == "auxpass":
                passive_voice.append(sent.text)
                break
            if token.pos_ == "ADV":
                adverb_overuse.append(token.text)
            if len(token.text) > 12:
                complex_words.append(token.text)

    score = max(0, 100 - (len(long_sentences) * 2 + len(passive_voice) * 3 + len(adverb_overuse)))
    return {
        "score": score,
        "issues": {
            "long_sentences": long_sentences,
            "passive_voice": passive_voice,
            "adverbs": adverb_overuse,
            "complex_words": complex_words,
        },
        "summary": "Higher score = better compliance with English writing guidelines."
    }
