from src.sensor import Sensor


def test_sensor_read():
    sensor = Sensor()
    value = sensor.read()
    assert isinstance(value, int)
