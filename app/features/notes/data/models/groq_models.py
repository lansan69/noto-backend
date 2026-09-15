
from pydantic import BaseModel
from typing import List

class GroqTranscriptElement(BaseModel):
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: List[int]
    temperature: int
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: int

class GroqTranscriptResponse(BaseModel):
    utterances:List[GroqTranscriptElement]