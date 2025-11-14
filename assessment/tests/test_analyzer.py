from app.services.analyzer import check_compliance

def test_compliance_check_structure():
    """Ensure the analyzer returns proper report structure."""
    text = (
        "This sentence is very long and actually it contains multiple clauses, "
        "which makes it harder to read and understand properly."
    )
    report = check_compliance(text)

    assert isinstance(report, dict)
    assert "score" in report
    assert "issues" in report
    assert "long_sentences" in report["issues"]
    assert report["score"] <= 100
