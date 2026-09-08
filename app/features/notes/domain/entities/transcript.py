class Utterance:
    def __init__(self, speaker: str, text: str, confidence: float, start: int, end: int):
        self.speaker = speaker
        self.text = text
        self.start = start
        self.end = end
        self.confidence = confidence

    @classmethod
    def from_json(cls, data: dict) -> "Utterance":
        return cls(
            speaker=data["speaker"],
            text=data["text"],
            confidence=data["confidence"],
            start=data["start"],
            end=data["end"],
        )

    def to_json(self) -> dict:
        return {
            "speaker": self.speaker,
            "text": self.text,
            "confidence": self.confidence,
            "start": self.start,
            "end": self.end,
        }

class TranscriptResult:
    def __init__(self, summary: str | None, action_items: list[str] | None, confidence: float, utterances: list[Utterance]):
        self.summary = summary
        self.action_items = action_items
        self.confidence = confidence
        self.utterances = utterances

    @classmethod
    def from_json(cls, data: dict) -> "TranscriptResult":
        utterances = [Utterance.from_json(u) for u in data.get("utterances", [])]
        return cls(
            summary=data.get("summary"),
            action_items=data.get("action_items"),
            confidence=data["confidence"],
            utterances=utterances,
        )

    def to_json(self) -> dict:
        return {
            "summary": self.summary,
            "action_items": self.action_items,
            "confidence": self.confidence,
            "utterances": [u.to_json() for u in self.utterances],
        }