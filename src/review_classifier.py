"""Probabilistic review classification using a 2-out-of-3 voting rule."""

from typing import Sequence, Tuple
import random


def validate_probabilities(values: Sequence[float]) -> None:
    if len(values) != 3:
        raise ValueError("Exactly three probabilities are required.")
    if any(value < 0 or value > 1 for value in values):
        raise ValueError("All probabilities must be between 0 and 1.")


def simulate_positive_reviews(
    probabilities: Sequence[float], count: int, rng: random.Random
) -> int:
    """Return the number of positive reviews classified as positive."""
    validate_probabilities(probabilities)
    if count <= 0:
        raise ValueError("Review count must be greater than zero.")

    correct = 0
    for _ in range(count):
        votes = sum(rng.random() < p for p in probabilities)
        if votes >= 2:
            correct += 1
    return correct


def simulate_negative_reviews(
    probabilities: Sequence[float], count: int, rng: random.Random
) -> int:
    """Return the number of negative reviews classified as negative."""
    validate_probabilities(probabilities)
    if count <= 0:
        raise ValueError("Review count must be greater than zero.")

    correct = 0
    for _ in range(count):
        votes = sum(rng.random() >= p for p in probabilities)
        if votes < 2:
            correct += 1
    return correct


def calculate_metrics(
    positive_correct: int,
    negative_correct: int,
    positive_count: int,
    negative_count: int,
) -> dict:
    """Calculate class-wise and overall accuracy."""
    if positive_count <= 0 or negative_count <= 0:
        raise ValueError("Both review counts must be greater than zero.")

    positive_accuracy = positive_correct / positive_count
    negative_accuracy = negative_correct / negative_count
    total = positive_count + negative_count
    overall_accuracy = (
        positive_correct + negative_correct
    ) / total

    return {
        "positive_accuracy": positive_accuracy,
        "negative_accuracy": negative_accuracy,
        "overall_accuracy": overall_accuracy,
    }


def run_simulation(
    alpha: Sequence[float],
    beta: Sequence[float],
    positive_count: int,
    negative_count: int,
    seed: int = 42,
) -> Tuple[int, int, dict]:
    """Run a reproducible simulation and return results."""
    rng = random.Random(seed)

    positive_correct = simulate_positive_reviews(
        alpha, positive_count, rng
    )
    negative_correct = simulate_negative_reviews(
        beta, negative_count, rng
    )

    metrics = calculate_metrics(
        positive_correct,
        negative_correct,
        positive_count,
        negative_count,
    )

    return positive_correct, negative_correct, metrics
