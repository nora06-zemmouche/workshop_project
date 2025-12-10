from anomaly_detector import AnomalyDetector
from sensor import Sensor
from mongodb_client import MongoDBClient

if __name__ == "__main__":
    # Exemple simple
    detector = AnomalyDetector(threshold=2.5)
    sensor = Sensor("TempSensor")
    db = MongoDBClient("my_db")

    data = [sensor.read() for _ in range(5)]
    print("Données capteur :", data)

    anomalies = detector.detect(data)
    print("Anomalies détectées :", anomalies)

    for i, value in enumerate(data):
        db.insert("sensor_data", {"value": value, "anomaly": anomalies[i]})

    print("Données insérées dans la base MongoDB (mongomock).")
