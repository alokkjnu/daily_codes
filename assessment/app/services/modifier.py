import re
import spacy

nlp = spacy.load("en_core_web_sm")

def correct_text(text: str) -> str:
    doc = nlp(text)
    new_sentences = []

    for sent in doc.sents:
        sent_text = sent.text

        # Remove common redundant adverbs
        sent_text = re.sub(r"\b(really|very|basically|actually|literally)\b", "", sent_text, flags=re.IGNORECASE)

        # Simplify passive voice heuristically
        sent_text = re.sub(r"\bwas\b\s+(\w+ed)", r"\1", sent_text)
        sent_text = re.sub(r"\bwere\b\s+(\w+ed)", r"\1", sent_text)

        # Shorten long sentences
        if len(sent) > 25:
            parts = sent_text.split(",")
            if len(parts) > 1:
                sent_text = ". ".join(parts[:2]) + "."

        new_sentences.append(sent_text.strip())

    return " ".join(new_sentences)
