# features/transcript/data/models/transcript_model.py

class UtteranceModel:
    def __init__(self, speaker: str, text: str, confidence: float, start: int, end: int):
        self.speaker = speaker
        self.text = text
        self.start = start
        self.end = end
        self.confidence = confidence

    @classmethod
    def from_json(cls, data: dict) -> "UtteranceModel":
        return cls(
            speaker=data["speaker"],
            text=data["text"],
            confidence=data["confidence"],
            start=data["start"],
            end=data["end"],
        )


class TranscriptModel:
    def __init__(self, summary: str | None, action_items: list[str] | None, confidence: float, utterances: list[UtteranceModel]):
        self.summary = summary
        self.action_items = action_items
        self.confidence = confidence
        self.utterances = utterances

    @classmethod
    def from_json(cls, data: dict) -> "TranscriptModel":
        return cls(
            summary=data.get("summary"),
            action_items=data.get("action_items"),
            confidence=data["confidence"],
            utterances=[UtteranceModel.from_json(u) for u in data.get("utterances", [])],
        )