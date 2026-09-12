import re
from enum import Enum
from pydantic import BaseModel, Field, field_validator, model_validator


class BlockTypeEnum(str, Enum):
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

_LEADING_DECORATION_RE = re.compile(
    r"^\s*(?:[•●▪‣◦∙](?=\s)|-(?=\s)|\*(?!\*)(?=\s)|[0-9]+[.)](?=\s)|⚠️|⚠|✅|📌|📝|❗|❕)\s*"
)

_EMOJI_ALLOWED_TYPES = {
    BlockTypeEnum.HEADING1,
    BlockTypeEnum.HEADING2,
    BlockTypeEnum.HEADING3,
    BlockTypeEnum.HEADING4,
    BlockTypeEnum.TABLE,
    BlockTypeEnum.CALLOUT,
}


class Block(BaseModel):
    type: BlockTypeEnum = Field(..., description="Type of content block. Use one of: HEADING1, HEADING2, HEADING3, HEADING4, PARAGRAPH, QUOTE, CALLOUT, BULLET_LIST_ITEM, NUMBERED_LIST_ITEM, TODO_LIST_ITEM, TABLE, CODE")
    emoji: str = Field(
        default="",
        description=(
            "Optional single emoji used as a visual marker. "
            "ONLY set this for HEADING1, HEADING2, HEADING3, HEADING4, TABLE, or CALLOUT blocks - "
            "use it to mark section headings, table topics, or important/critical statements. "
            "Leave empty (\"\") for every other block type (PARAGRAPH, QUOTE, BULLET_LIST_ITEM, "
            "NUMBERED_LIST_ITEM, TODO_LIST_ITEM, CODE). Never put the emoji inside \"text\"."
        ),
    )
    text: str = Field(
        ...,
        description=(
            "Text content of the block. Inline rich-text markers are allowed: **bold** for key terms, "
            "`backtick highlight` for Notion-style emphasis on standout words/numbers, and __underline__ "
            "for the single most important phrase in the block. "
            "Never prepend bullet symbols, numbering, or icons - the 'type' field already conveys that."
        ),
        min_length=1,
    )    
    
    @field_validator("text")
    @classmethod
    def strip_leading_decoration(cls, value: str) -> str:
        return _LEADING_DECORATION_RE.sub("", value).strip()

    @model_validator(mode="after")
    def clear_emoji_for_disallowed_types(self) -> "Block":
        if self.type not in _EMOJI_ALLOWED_TYPES:
            self.emoji = ""
        return self

class NotesModel(BaseModel):
    language: str = Field(..., description="Lenguaje detectado")
    title: str = Field(..., description="Title of the generated notes", min_length=1)
    notes_column: list[Block] = Field(..., description="List of content blocks containing the detailed notes structured with headings, paragraphs, lists, and other block types")
    action_items: list[str] = Field(..., description="List of specific tasks, action items, or decisions that need to be completed or implemented based on the class discussion")
    summary: str = Field(..., description="Brief summary of the main points, key concepts, and takeaways from the class session")
    support_material: list[str] = Field(..., description="List of recommended resources, references, books, links, or materials for further study and learning recommended during the class")
    homework: list[str] = Field(..., description="List of homework assignments, exercises, or practice problems assigned during the class")
    