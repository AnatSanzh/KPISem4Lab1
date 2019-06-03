from record import PhoneDirectoryRecord
from abc import abstractmethod


class RecordStorage:
    """Abstract class that defines interface for storage classes"""

    @abstractmethod
    def add(self, number: str, name: str, address: str) -> str:
        pass

    @abstractmethod
    def remove(self, number: str) -> str:
        pass

    @abstractmethod
    def get(self, number: str) -> PhoneDirectoryRecord:
        pass

    @abstractmethod
    def clear(self) -> str:
        pass

    @abstractmethod
    def update(self, number: str, name: str, address: str) -> str:
        pass

    @abstractmethod
    def list(self, offset: int, count: int) -> list:
        pass
