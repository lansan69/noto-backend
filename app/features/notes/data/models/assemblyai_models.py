# features/notes/data/models/transcript_models.py
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class RequestActionItemsModel(BaseModel):
    effort: str
    include_decisions: bool


class RequestSummarizationModel(BaseModel):
    summary_type: str
    effort: str


class RequestModel(BaseModel):
    summarization: RequestSummarizationModel
    action_items: RequestActionItemsModel


class ItemModel(BaseModel):
    action_item: str
    quote: str
    timestamp: int


class ResponseActionItemsModel(BaseModel):
    items: List[ItemModel]
    effort: str
    status: str


class SummaryElementModel(BaseModel):
    start: int
    end: int
    text: str


class ResponseSummarizationModel(BaseModel):
    block_summary: str
    summary_type: str
    effort: str
    status: str
    summary: List[SummaryElementModel]


class ResponseModel(BaseModel):
    summarization: ResponseSummarizationModel
    action_items: ResponseActionItemsModel


class SpeechUnderstandingModel(BaseModel):
    request: RequestModel
    response: ResponseModel


class WordModel(BaseModel):
    text: str
    confidence: float
    start: int
    end: int


class UtteranceModel(BaseModel):
    speaker: Optional[str] = None
    text: str
    confidence: float
    start: int
    end: int
    words: Optional[List[WordModel]] = None


class TranscriptResultModel(BaseModel):
    id: UUID
    language_code: str
    speech_understanding: Optional[SpeechUnderstandingModel] = None
    status: str
    text: str
    words: Optional[List[WordModel]] = None
    utterances: Optional[List[UtteranceModel]] = None
    confidence: float