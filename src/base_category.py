from abc import ABC, abstractmethod


class BaseCategory(ABC):

    @abstractmethod
    def add_product(self, *args, **kwargs):
        pass
