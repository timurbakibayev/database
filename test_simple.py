from field import Field
from row import Row


def test_field():
    field1 = Field(name="id", field_type="int")
    assert isinstance(field1, Field)
    assert field1.name == "id"
    assert field1.field_type == "int"


def test_create_row():
    id_ = Field(name="id", field_type="int")
    name = Field(name="name", field_type="str")

    row1 = Row(
        data={
            "id": 1,
            "name": "John",
        },
        fields=[
            id_,
            name,
        ]
    )

    row2 = Row(
        data={
            "id": 2,
            "name": "Bob",
        },
        fields=[
            id_,
            name,
        ]
    )

    assert isinstance(row1, Row)
    assert isinstance(row2, Row)

    assert row1.data["id"] == 1
    assert row1["id"] == 1
    assert row1["name"] == "John"
    assert row2["id"] == 2
    assert row2["name"] == "Bob"

