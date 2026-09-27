# Probabilistic Review Classifier

A Python-based probabilistic simulation for classifying positive and negative
reviews using three independent probability-based classifiers and a
**2-out-of-3 voting rule**.

## Project Overview

This project simulates how multiple simple classifiers can be combined to
make a final review-classification decision. The original project accepts
three alpha values, three beta values, and the number of positive and
negative reviews, then estimates class-wise accuracy through repeated
random trials.

The project has been reorganized into reusable functions, reproducible
experiments, automated tests, and result analysis.

## How It Works

### Positive reviews

For each positive review, each of the three classifiers independently
produces a positive vote according to its alpha probability.

A review is classified as positive when at least **2 of the 3 classifiers**
vote positive.

### Negative reviews

For each negative review, each classifier produces the corresponding
probability-based outcome using its beta value.

A review is classified as negative when fewer than 2 classifiers produce a
positive vote.

## Parameters

- `alpha1`, `alpha2`, `alpha3`: probabilities used for positive-review simulation
- `beta1`, `beta2`, `beta3`: probabilities used for negative-review simulation
- Positive review count
- Negative review count

## Project Structure

```text
probabilistic-review-classifier/
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── src/
│   └── review_classifier.py
├── notebooks/
│   └── analysis.ipynb
├── tests/
│   └── test_classifier.py
└── results/
    ├── sample_results.txt
    ├── accuracy_plot.png
    ├── confusion_matrix.png
    └── comparison_plot.png
```

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/probabilistic-review-classifier.git
cd probabilistic-review-classifier
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Run Tests

```bash
pytest
```

## Example

Example parameters:

```text
alpha = [0.8, 0.7, 0.9]
beta  = [0.2, 0.3, 0.1]
positive reviews = 100
negative reviews = 100
seed = 42
```

The exact simulated result is reproducible when the same seed and inputs
are used.

## Results

The `results/` folder contains sample outputs and visual analysis generated
from the simulation.

## Limitations

This project is a probabilistic simulation rather than a trained machine
learning model. It does not learn classifier parameters from a real review
dataset, and it does not perform natural-language processing on review text.

## Future Improvements

- Use a real review dataset.
- Add NLP-based sentiment classification.
- Compare the probabilistic voting method with standard ML models.
- Add precision, recall, F1-score, and a true confusion matrix based on
  labelled data.
- Build a small web interface for interactive predictions.

## Technologies

- Python
- Random simulation
- Matplotlib
- Jupyter Notebook
- Pytest

## Author

**Banasree Maji**

B.Tech in Computer Science & Engineering
