# features/notes/data/models/note_draft_model.py

class BlockDraftModel:
    def __init__(self, type: str, content: str):
        self.type = type
        self.content = content

    @classmethod
    def from_json(cls, data: dict) -> "BlockDraftModel":
        return cls(
            type=data["type"],
            content=data["content"],
        )


class NoteDraftModel:
    def __init__(self, title: str, content: list[BlockDraftModel]):
        self.title = title
        self.content = content

    @classmethod
    def from_json(cls, data: dict) -> "NoteDraftModel":
        return cls(
            title=data["title"],
            content=[BlockDraftModel.from_json(b) for b in data.get("content", [])],
        )