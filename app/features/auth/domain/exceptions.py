# domain/exceptions.py

class DomainError(Exception):
    """Base class for all domain-level errors."""
    pass


class InvalidCredentialsError(DomainError):
    """Raised when sign-in credentials don't match any user."""
    pass