from typing import Tuple

from table import Table, Field


class Database:
    def __init__(self, name: str):
        self.name = name
        self.tables: list[Table] = list()

    def add_table(self, fields_descriptions: list[Tuple[str, str]], name: str) -> Table:
        table = Table(name=name)
        for field in fields_descriptions:
            name, field_type = field
            table.add_field(Field(name=name, field_type=field_type))
        self.tables.append(table)
        return table

    def __str__(self) -> str:
        return f"Table: {self.name}, {len(self.tables)} tables"

    def get_tables(self) -> list[Table]:
        return self.tables
