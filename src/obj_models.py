class Story:
    def __init__(self, story_id: int, story: str, model: str = None, temperature: float = None):
        self.id = story_id
        self.story = story
        self.model = model
        self.temperature = temperature

    def from_json(self, json_obj: dict):
        self.id = json_obj["id"]
        self.story = json_obj["story"]
        self.model = json_obj["model"]
        self.temperature = json_obj["temperature"]

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "story": self.story,
            "model": self.model,
            "temperature": self.temperature
        }

    def __str__(self):
        return f"Story(id={self.id}, story={self.story}, model={self.model}, temperature={self.temperature})"


class Criterion:
    def __init__(self, name: str, criterion: str):
        self.name = name
        self.criterion = criterion

    def from_json(self, json_obj: dict):
        self.name = json_obj["name"]
        self.criterion = json_obj["criterion"]

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "criterion": self.criterion
        }

    def __str__(self):
        return f"Criterion(name={self.name}, criterion={self.criterion})"
