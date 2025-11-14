from app.services.modifier import correct_text

def test_modifier_reduces_adverbs():
    text = "It is really very important to actually complete the work."
    result = correct_text(text)
    assert "really" not in result.lower()
    assert "actually" not in result.lower()
