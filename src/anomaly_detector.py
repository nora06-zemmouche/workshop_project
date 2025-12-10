import statistics


class AnomalyDetector:
    def __init__(self, threshold=3.0):
        self.threshold = threshold

    def is_anomaly(self, value, history):
        if len(history) < 2:
            return False
        mean = statistics.mean(history)
        std = statistics.pstdev(history)
        if std == 0:
            return False
        z = abs((value - mean) / std)
        return z >= self.threshold

    def detect(self, data):
        results = []
        for i, value in enumerate(data):
            history = data[:i] + data[i+1:]
            results.append(self.is_anomaly(value, history))
        return results
