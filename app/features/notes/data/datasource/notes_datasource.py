# data/datasources/notes_datasource.py

import logging
from app.features.notes.domain.entities.transcript_entities import TranscriptResult, SummaryElement, ActionItem, Utterance
from app.features.notes.data.models.notes_models import NotesModel
from openai import AsyncOpenAI

# Initialize logger
logger = logging.getLogger(__name__)

class NotesDatasource:
    def __init__(self, openai_client: AsyncOpenAI, alibaba_models: list[str]):
        self._openai_client = openai_client
        self.alibaba_models = alibaba_models
    
    async def select_model(self):
        models = await self._openai_client.models.list()
        available_ids = {model.id for model in models.data}
        for m in self.alibaba_models:
            if m in available_ids:
                return m
        raise ValueError("No available valid model")
    
    def formatUtterances(self, utterances: list[Utterance]):
        return "\n".join(
            f"[{u.start}-{u.end}]{u.speaker}: {u.text}"
            for u in utterances
        )
    
    def formatActionItems(self, action_items: list[ActionItem]):
        return "\n".join(
            f"[{item.timestamp}] {item.action_item} | {item.quote} |"
            for item in action_items
        )
    
    def formatSummary(self, summary: list[SummaryElement]) -> str:
        return "\n".join(
            f"[ {item.start} - {item.end} ] {item.text}"
            for item in summary
        )
    
    def format_transcript(self, transcript: TranscriptResult):
        sections = []

        if transcript.summary:
            sections.append(f"<summary>\n{self.formatSummary(transcript.summary)}\n</summary>")
        if transcript.action_items:
            sections.append(f"<action_items>\n{self.formatActionItems(transcript.action_items)}\n</action_items>")
        if transcript.utterances:
            sections.append(f"<utterances>\n{self.formatUtterances(transcript.utterances)}\n</utterances>")
        elif transcript.text:
            sections.append(f"<transcript>\n{transcript.text}\n</transcript>")

        return "\n".join(sections)
    
    async def create_note(self, system_prompt:str, transcript:TranscriptResult) -> NotesModel:
        logger.debug("Verificando el modelo.")
        selected_model = await self.select_model()
        formatted_input = self.format_transcript(transcript) 
        try:
            logger.debug("Iniciando el análisis.")
            completion = await self._openai_client.beta.chat.completions.parse(
                model=selected_model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": f"Create structured notes from this transcript:\n\n{formatted_input}"
                    }
                ],
                response_format=NotesModel,
            )
            
            if completion.choices[0].message.parsed:
                logger.debug("Análisis exitoso")
                return completion.choices[0].message.parsed
            else: 
                logger.exception("Error en el análisis")
                raise ValueError(f"Analysis didn't complete successfully: {completion.choices[0].message.content}") 
        except Exception as e:
            logger.exception(f"Error en el análisis: {e}")
            raise ValueError(f"Failed to create note: {str(e)}") from e

        