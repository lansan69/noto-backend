from unittest.mock import Mock
from fastapi.testclient import TestClient
from app.main import app
from app.api.v1.notes import notes as transcript_module

client = TestClient(app)

def test_create_transcript_test(monkeypatch):
    monkeypatch.setattr(
        transcript_module.transcriber, "upload_file",
        Mock(return_value="https://fake-upload-url")
    )
    monkeypatch.setattr(
        transcript_module.transcriber, "transcribe",
        Mock(return_value=Mock(text="fake transcribed text", status="completed"))
    )

    headers = {"user-id": "alan", "username": "alan", "host": "example.com"}
    files = {"audio_file": ("test.mp3", b"fake audio bytes", "audio/mp3")}
    response = client.post("/transcript/", headers=headers, files=files)
    assert response.status_code == 200
    assert "transcript" in response.json()
