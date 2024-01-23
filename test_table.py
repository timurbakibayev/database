from database import Database


def test_table():
    db = Database(name="cars and cats")
    cars = db.add_table(fields_descriptions=[("id", "int"), ("name", "str")], name="cars")

    cars.insert({"id": 1, "name": "Toyota"})
    cars.insert({"id": 2, "name": "Mercedes"})

    rows = cars.get_rows()
    assert cars.rows_count == 2
    assert rows[0]["id"] == 1
    assert rows[0]["name"] == "Toyota"
    assert rows[1]["id"] == 2
    assert rows[1]["name"] == "Mercedes"
