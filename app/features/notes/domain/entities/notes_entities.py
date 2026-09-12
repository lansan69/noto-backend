# domain/entities/note_draft.py

from enum import Enum


class BlockType(Enum):
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    PARAGRAPH = "paragraph"
    QUOTE = "quote"
    CALLOUT = "callout"
    BULLET_LIST_ITEM = "bullet_list_item"
    NUMBERED_LIST_ITEM = "numbered_list_item"
    TODO_LIST_ITEM = "todo_list_item"
    TABLE = "table"
    CODE = "code"


class BlockDraft:
    def __init__(self, type: BlockType, text: str, emoji: str = ""):
        if not text.strip():
            raise ValueError("text cannot be empty")
        self.type = type
        self.text = text
        self.emoji = emoji

    @classmethod
    def from_json(cls, data: dict) -> "BlockDraft":
        return cls(
            type=BlockType(data["type"]),
            text=data["text"],
            emoji=data.get("emoji", ""),
        )

    def to_json(self) -> dict:
        return {
            "type": self.type.value,
            "emoji": self.emoji,
            "text": self.text,
        }


class NoteDraft:
    def __init__(
        self,
        language: str,
        title: str,
        summary: str,
        content: list[BlockDraft],
        action_items: list[str] | None = None,
        support_material: list[str] | None = None,
        homework: list[str] | None = None,
    ):
        if not title.strip():
            raise ValueError("title cannot be empty")
        if not language.strip():
            raise ValueError("language cannot be empty")
        self.title = title
        self.content = content
        self.language = language
        self.summary = summary
        self.action_items = action_items or []
        self.support_material = support_material or []
        self.homework = homework or []

    @classmethod
    def from_json(cls, data: dict) -> "NoteDraft":
        return cls(
            title=data["title"],
            content=[BlockDraft.from_json(b) for b in data.get("notes_column", [])],
            language=data["language"],
            summary=data.get("summary", ""),
            action_items=data.get("action_items", []),
            support_material=data.get("support_material", []),
            homework=data.get("homework", []),
        )

    def to_json(self) -> dict:
        return {
            "title": self.title,
            "language": self.language,
            "notes_column": [b.to_json() for b in self.content],
            "summary": self.summary,
            "action_items": self.action_items,
            "support_material": self.support_material,
            "homework": self.homework,
        }
