# data/supabase/user_validation_impl.py
from app.features.notes.data.datasource.transcript_datasource import TranscriptionDatasource
from app.features.notes.domain.repository.transcript import TranscriptRepository
from app.features.notes.domain.exceptions import TranscriptError
from app.features.notes.data.models.transcript_models import TranscriptResultModel
from app.features.notes.domain.entities.transcript_entities import TranscriptResult, Utterance, SummaryElement, ActionItem

class TranscriptResultImpl(TranscriptRepository):
    def __init__(self, datasource: TranscriptionDatasource):
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
            model = await self._datasource.create_transcript(audio_bytes=audio_bytes)
            return self._to_domain(model)
        except TranscriptError:
            raise
        except Exception as e:
            raise TranscriptError(f"Failed to transcribe audio: {str(e)}") from e