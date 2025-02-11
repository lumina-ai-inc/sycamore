from abc import ABC, abstractmethod
from typing import Optional

from sycamore.utils.cache import Cache


class LLM(ABC):
    def __init__(self, model_name, cache: Optional[Cache] = None):
        self._model_name = model_name
        self._cache = cache

    @abstractmethod
    def generate(self, *, prompt_kwargs: dict, llm_kwargs: Optional[dict] = None) -> str:
        pass

    @abstractmethod
    def is_chat_mode(self) -> bool:
        pass


class FakeLLM(LLM):
    """Useful for tests where the fake LLM needs to run in a ray function because mocks are not serializable"""

    def __init__(self, *, return_value="trivial"):
        super().__init__("trivial")
        self._return_value = return_value

    def generate(self, *, prompt_kwargs: dict, llm_kwargs: Optional[dict] = None) -> str:
        return self._return_value

    def is_chat_mode(self) -> bool:
        return False
