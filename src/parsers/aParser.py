"""Parser interface"""

from abc import ABC, abstractmethod
from typing import List
from common.error import Error


class Parser(ABC):
    targetDir = ""

    def __init__(self, targetDir):
        self.targetDir = targetDir

    @abstractmethod
    def parse(self) -> List[Error]:
        pass
