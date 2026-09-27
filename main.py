"""Command-line interface for the probabilistic review classifier."""

from src.review_classifier import run_simulation


def read_probability(name: str) -> float:
    while True:
        try:
            value = float(input(f"Enter {name} (0-1): "))
            if 0 <= value <= 1:
                return value
            print("Please enter a value between 0 and 1.")
        except ValueError:
            print("Please enter a valid number.")


def read_count(name: str) -> int:
    while True:
        try:
            value = int(input(f"Enter number of {name} reviews: "))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    print("\nProbabilistic Review Classifier")
    print("Three classifiers + 2-out-of-3 voting rule\n")

    alpha = [
        read_probability("alpha1"),
        read_probability("alpha2"),
        read_probability("alpha3"),
    ]

    beta = [
        read_probability("beta1"),
        read_probability("beta2"),
        read_probability("beta3"),
    ]

    positive_count = read_count("positive")
    negative_count = read_count("negative")

    positive_correct, negative_correct, metrics = run_simulation(
        alpha, beta, positive_count, negative_count
    )

    print("\n--- Results ---")
    print(f"Positive accuracy: {metrics['positive_accuracy'] * 100:.2f}%")
    print(f"Negative accuracy: {metrics['negative_accuracy'] * 100:.2f}%")
    print(f"Overall accuracy:  {metrics['overall_accuracy'] * 100:.2f}%")
    print(f"Positive correct:  {positive_correct}/{positive_count}")
    print(f"Negative correct:  {negative_correct}/{negative_count}")


if __name__ == "__main__":
    main()
