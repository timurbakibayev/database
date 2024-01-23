from typing import Any

from row import Row, Field


class Table:
    def __init__(self, name: str):
        self.name = name
        self.fields: list[Field] = list()
        self.rows: list[Row] = list()
        self.rows_count = 0

    def get_rows(self) -> list[Row]:
        return self.rows

    def add_field(self, field: Field):
        self.fields.append(field)

    def remove_field(self, field: Field):
        self.fields = [
            field1
            for field1 in self.fields
            if field1.name != field.name
        ]

        # new_fields = list()
        # for field1 in self.fields:
        #     if field1.name != field.name:
        #         new_fields.append(field1)
        # self.fields = new_fields

    def get_fields(self) -> list[Field]:
        return self.fields

    def _insert_row(self, row: Row):
        self.rows.append(row)
        self.rows_count += 1

    def insert(self, data: dict[str, Any]):
        new_row = Row(
            data=data,
            fields=self.fields
        )
        self._insert_row(new_row)
