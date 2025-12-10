from src.anomaly_detector import AnomalyDetector


def test_anomaly():
    detector = AnomalyDetector(threshold=2.5)
    data = [10, 12, 11, 20, 13]
    result = detector.detect(data)
    assert all(isinstance(r, bool) for r in result)
