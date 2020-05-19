"""Parser interface, should be implemented by all parsers"""

from abc import ABC, abstractmethod
from typing import List
from common.error import Error


class Parser(ABC):

    def __init__(self, targetDir):
        self.targetDir = targetDir

    @abstractmethod
    def parse(self) -> List[Error]:
        pass
