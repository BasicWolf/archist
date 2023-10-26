from abc import abstractmethod, ABC


class Validator(ABC):
    @abstractmethod
    def validate(self, node) -> bool:
        ...
