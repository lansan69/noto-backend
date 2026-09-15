# data/repository/alibaba_notes_repository_impl.py
from app.features.notes.data.datasource.alibaba_notes_datasource import AlibabaNotesDatasource
from app.features.notes.domain.repository.notes_repository import NotesRepository
from app.features.notes.domain.entities.notes_entities import NoteDraft, BlockDraft, BlockType
from app.features.notes.domain.exceptions import AnalysisError
from app.features.notes.data.models.notes_models import NotesModel, Block
from app.features.notes.domain.entities.transcript_entities import TranscriptResult

class AlibabaNotesRepositoryImpl(NotesRepository):
    def __init__(self, datasource: AlibabaNotesDatasource):
        self._datasource = datasource

    def _block_to_domain(self, block: Block) -> BlockDraft:
        return BlockDraft(
            type=BlockType(block.type.value),
            text=block.text,
            emoji=block.emoji,
        )

    def _to_domain(self, model: NotesModel) -> NoteDraft:
        return NoteDraft(
            language=model.language,
            title=model.title,
            summary=model.summary,
            content=[self._block_to_domain(b) for b in model.notes_column],
            action_items=model.action_items,
            support_material=model.support_material,
            homework=model.homework,
        )

    async def create_note(self, transcript: TranscriptResult, system_prompt: str) -> NoteDraft:
        try:
            model = await self._datasource.create_note(transcript=transcript, system_prompt=system_prompt)
            return self._to_domain(model)
        except AnalysisError:
            raise
        except Exception as e:
            raise AnalysisError(f"Failed to generate note: {str(e)}") from e