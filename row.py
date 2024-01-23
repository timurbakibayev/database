from typing import Any

from field import Field


class Row:
    def __init__(self, data: dict[str, Any], fields: list[Field]):
        self.data = data
        self.fields = fields
        # TODO: check fields

    def __str__(self):
        output = "Row:\n"
        for field in self.fields:
            output += f"  {field.name}: {self.data[field.name]}\n"

    def __getitem__(self, item):
        return self.data[item]
