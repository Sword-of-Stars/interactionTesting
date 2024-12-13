# Interaction Testing for Ensuring Input Diversity for Training Classification Models
### CDT Matthew Wanta and Nikolas Dykstra

## Installation and Setup

The following code is written in Python 3.12.

```shell
git clone https://github.com/Sword-of-Stars/interactionTesting
```

To install the requirements for this project, run the following command:

```shell
pip install -r requirements.txt
```

## Code Overview
This code explores applies the principles of interaction testing to ensuring input diversity for neural networks and random forest classifiers. We analyze two datasets: a diabetes predictor dataset and a housing price dataset. We begin by comparing the performance of a model trained on a full dataset to one trained on a covering dataset of smaller size, and found that the latter model saw lower performance. Then, instead of exploring perfect coverage, we explore percent coverage; describing the percentage of the interactions present in the whole dataset are represented in the subset. We found a weak positive correlation between model performance and percent coverage, but results were largely inconclusive.

Further documentation can be found in the code main body, `main.ipynb`