# domain/entities/note_draft.py

from enum import Enum


class BlockType(Enum):
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    PARAGRAPH = "paragraph"
    BULLET_LIST_ITEM = "bullet_list_item"
    NUMBERED_LIST_ITEM = "numbered_list_item"
    TODO_LIST_ITEM = "todo_list_item"
    TABLE = "table"
    CODE = "code"
    QUOTE = "quote"
    CALLOUT = "callout"


class BlockDraft:
    def __init__(self, type: BlockType, content: str):
        if not content.strip():
            raise ValueError("content cannot be empty")
        self.type = type
        self.content = content

    @classmethod
    def from_json(cls, data: dict) -> "BlockDraft":
        return cls(
            type=BlockType(data["type"]),
            content=data["content"],
        )

    def to_json(self) -> dict:
        return {
            "type": self.type.value,
            "content": self.content,
        }


class NoteDraft:
    def __init__(self, title: str, content: list[BlockDraft]):
        if not title.strip():
            raise ValueError("title cannot be empty")
        self.title = title
        self.content = content

    @classmethod
    def from_json(cls, data: dict) -> "NoteDraft":
        return cls(
            title=data["title"],
            content=[BlockDraft.from_json(b) for b in data.get("content", [])],
        )

    def to_json(self) -> dict:
        return {
            "title": self.title,
            "content": [b.to_json() for b in self.content],
        }