# data/repository/transcript_repository_impl.py
from app.features.notes.data.datasource.transcript_datasource import AssemblyAITranscriptionDatasource, GroqTranscriptionDatasource
from app.features.notes.domain.repository.transcript import TranscriptRepository
from app.features.notes.domain.exceptions import TranscriptError
from app.features.notes.data.models.assemblyai_models import TranscriptResultModel
from app.features.notes.data.models.groq_models import GroqTranscriptResponse
from app.features.notes.domain.entities.transcript_entities import TranscriptResult, Utterance, SummaryElement, ActionItem

class AssemblyAITranscriptResultImpl(TranscriptRepository):
    def __init__(self, datasource: AssemblyAITranscriptionDatasource):
        self._datasource = datasource
    
    def _to_domain(self, model: TranscriptResultModel) -> TranscriptResult:
        summary = model.speech_understanding.response.summarization.summary if model.speech_understanding else None
        action_items = model.speech_understanding.response.action_items.items if model.speech_understanding else None
        utterances = model.utterances if model.utterances else None
        
        return TranscriptResult(
            summary=list(SummaryElement(
                    start=s.start,
                    end=s.end,
                    text=s.text
                ) for s in summary or []
            ), 
            action_items=list(ActionItem(
                    action_item=i.action_item,
                    quote=i.quote,
                    timestamp=i.timestamp
                )for i in action_items or []
            ),
            confidence=model.confidence,
            utterances=list(Utterance(
                    speaker=u.speaker or "",
                    text=u.text,
                    confidence=u.confidence,
                    start=u.start,
                    end=u.end
                ) for u in utterances or []
            ),
            text=model.text,
            language_code=model.language_code,
        )
    
    async def create_transcript(self, audio_bytes: bytes) -> TranscriptResult:
        try:
            model = await self._datasource.create_transcript_assemblyai(audio_bytes=audio_bytes)
            return self._to_domain(model)
        except TranscriptError:
            raise
        except Exception as e:
            raise TranscriptError(f"Failed to transcribe audio: {str(e)}") from e

class GroqTranscriptResultImpl(TranscriptRepository):
    def __init__(self, datasource: GroqTranscriptionDatasource):
        self._datasource = datasource
    
    def _to_ms(self, seconds: float) -> int:
        return int(seconds * 1000)

    def _to_domain(self, model: GroqTranscriptResponse) -> TranscriptResult:
        return TranscriptResult(
            language_code="",
            summary=[],
            action_items=[],
            confidence=0.0,
            utterances=list(Utterance(
                    speaker= "",
                    text=u.text,
                    confidence=0.0,
                    start=self._to_ms(u.start),
                    end=self._to_ms(u.end)
                ) for u in model.utterances or []
            ),
            text="".join(u.text for u in model.utterances or [])
        )
    
    async def create_transcript(self, audio_bytes: bytes) -> TranscriptResult:
        try:
            model = await self._datasource.create_transcript_groq(audio_bytes=audio_bytes)
            return self._to_domain(model)
        except TranscriptError:
            raise
        except Exception as e:
            raise TranscriptError(f"Failed to transcribe audio: {str(e)}") from e