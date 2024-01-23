class Field:
    def __init__(self, name: str, field_type: str):
        self.name = name
        self.field_type = field_type

    def __str__(self) -> str:
        return f"Field: {self.name}: {self.field_type}"
