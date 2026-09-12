# domain/entities/transcript.py

class SummaryElement:
    def __init__(self, start: int, end: int, text: str,):
        self.start = start
        self.end = end
        self.text = text
    
    def to_json(self) -> dict:
        return {"start": self.start, "end": self.end, "text": self.text}


class ActionItem:
    def __init__(self, action_item: str, quote: str, timestamp: int):
        self.action_item = action_item
        self.quote = quote
        self.timestamp = timestamp

    def to_json(self) -> dict:
        return {
            "action_item": self.action_item,
            "quote": self.quote,
            "timestamp": self.timestamp,
        }


class Utterance:
    def __init__(self, speaker: str, text: str, confidence: float, start: int, end: int):
        self.speaker = speaker
        self.text = text
        self.confidence = confidence
        self.start = start
        self.end = end

    def to_json(self) -> dict:
        return {
            "speaker": self.speaker,
            "text": self.text,
            "confidence": self.confidence,
            "start": self.start,
            "end": self.end,
        }


class TranscriptResult:
    def __init__(
        self,
        language_code:str,
        summary: list[SummaryElement],
        action_items: list[ActionItem],
        confidence: float,
        utterances: list[Utterance],
        text: str,
    ):
        self.language_code = language_code
        self.summary = summary
        self.action_items = action_items
        self.confidence = confidence
        self.utterances = utterances
        self.text = text

    def to_json(self) -> dict:
        return {
            "language": self.language_code,
            "summary": [e.to_json() for e in self.summary],
            "action_items": [i.to_json() for i in self.action_items],
            "confidence": self.confidence,
            "utterances": [u.to_json() for u in self.utterances],
            "text": self.text,
        }