"""Random Forest model wrapper."""

from sklearn.ensemble import RandomForestClassifier

def train_rf(X, y, **kwargs):
    clf = RandomForestClassifier(**kwargs)
    clf.fit(X, y)
    return clf
