import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score

class AnomalyDetector:
    def __init__(self, model, threshold=0.5):
        self.model = model
        self.threshold = threshold

    def detect_anomalies(self, X):
        y_pred = self.model.predict(X)
        anomalies = np.where(y_pred < self.threshold)[0]
        return anomalies

class PerformanceMonitor:
    def __init__(self, model):
        self.model = model
        self.accuracy_history = []

    def monitor_performance(self, X, y):
        y_pred = self.model.predict(X)
        accuracy = accuracy_score(y, np.argmax(y_pred, axis=1))
        self.accuracy_history.append(accuracy)
        return accuracy
