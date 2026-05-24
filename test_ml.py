import pytest
# TODO: add necessary import
import numpy as np
from ml.model import (
    train_model,
    inference,
    compute_model_metrics
)

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    # add description for the first test
    # Test that train_model returns a trained model.
    """
    # Your code here
    X_train = np.array([[0, 1], [1, 0]])
    y_train = np.array([0, 1])

    model = train_model(X_train, y_train)

    assert model is not None


# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
    # add description for the second test
    # Test that inference returns predictions.
    """
    # Your code here
    X_train = np.array([[0, 1], [1, 0]])
    y_train = np.array([0, 1])

    model = train_model(X_train, y_train)

    preds = inference(model, X_train)

    assert len(preds) == 2


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # add description for the third test
    # Test that compute_model_metrics returns floats.
    """
    # Your code here
    y = np.array([1, 0, 1])
    preds = np.array([1, 0, 0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
