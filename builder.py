from typing import ClassVar
from .chatbot import IChatbot


class ChatbotBuilder:

    def __init__(self):
        self.cls = None
        self.cfg = {}

    def use(self, cls: ClassVar[IChatbot]):
        self.cls = cls
        return self

    def set(self, key: str, val: any):
        self.cfg[key] = val
        return self

    def new(self) -> IChatbot:
        return self.cls(self.cfg)