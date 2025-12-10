from src.mongodb_client import MongoDBClient


def test_insert_and_find():
    db = MongoDBClient("test_db")
    doc = {"name": "test", "value": 123}
    result = db.insert("test_collection", doc)
    assert result.inserted_id is not None

    found = db.find("test_collection", {"name": "test"})
    assert len(found) == 1
    assert found[0]["value"] == 123
f 