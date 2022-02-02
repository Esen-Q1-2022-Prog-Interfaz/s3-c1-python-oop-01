class Task:
    def __init__(self, description: str, isFinished=False, id=0) -> None:
        self.id = id
        self.description = description
        self.isFinished = isFinished

    def changeStatus(self, value):
        self.isFinished = value

    def __repr__(self) -> str:
        return f"Task('{self.description}', {self.isFinished}, {self.id})"
