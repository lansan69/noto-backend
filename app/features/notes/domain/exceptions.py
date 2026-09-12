# domain/exceptions.py

class DomainError(Exception):
    """Base class for all domain-level errors."""
    pass

class UploadError(DomainError):
    """Raised when upload fails for any reason."""
    pass

class TranscriptError(DomainError):
    """Raised when transcirpt process fails."""
    pass

class AnalysisError(DomainError):
    """Raised when analysis fails"""
    pass