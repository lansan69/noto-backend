class User:
    def __init__(self, user_id: str, nickname: str, name: str, last_name: str, credits: float = 0.0):
        if not name.strip():
            raise ValueError("name cannot be empty")
        if not last_name.strip():
            raise ValueError("last_name cannot be empty")
        if not nickname.strip():
            raise ValueError("nickname cannot be empty")

        self._user_id = user_id
        self.nickname = nickname
        self.name = name
        self.last_name = last_name
        self.credits = credits

    @property
    def user_id(self) -> str:
        return self._user_id

    @classmethod
    def from_json(cls, data: dict) -> "User":
        return cls(
            user_id=data["user_id"],
            nickname=data["nickname"],
            name=data["name"],
            last_name=data["last_name"],
            credits=data.get("credits", 0.0),
        )

    def to_json(self) -> dict:
        return {
            "user_id": self.user_id,
            "nickname": self.nickname,
            "name": self.name,
            "last_name": self.last_name,
            "credits": self.credits,
        }

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash(self.user_id)

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, nickname={self.nickname!r})"