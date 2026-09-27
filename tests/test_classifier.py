import random
import pytest

from src.review_classifier import (
    calculate_metrics,
    run_simulation,
    validate_probabilities,
)


def test_probability_validation():
    validate_probabilities([0.2, 0.5, 0.8])


def test_invalid_probability():
    with pytest.raises(ValueError):
        validate_probabilities([0.2, 1.2, 0.8])


def test_metrics():
    metrics = calculate_metrics(80, 90, 100, 100)
    assert metrics["positive_accuracy"] == 0.80
    assert metrics["negative_accuracy"] == 0.90
    assert metrics["overall_accuracy"] == 0.85


def test_reproducibility():
    first = run_simulation([0.8, 0.7, 0.9], [0.2, 0.3, 0.1], 100, 100, seed=42)
    second = run_simulation([0.8, 0.7, 0.9], [0.2, 0.3, 0.1], 100, 100, seed=42)
    assert first == second
