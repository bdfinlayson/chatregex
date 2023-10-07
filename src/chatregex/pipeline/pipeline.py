from re import Pattern
from typing import Self, Dict, Union

from src.chatregex.pipeline.text_parser import TextParser


class Pipeline:
    def __int__(self, file_path: str, patterns: Dict[str, Pattern], occurrence_n=1):
        self.file_path = file_path
        self.patterns = patterns
        self.occurrence_n = occurrence_n
        self.occurrences: Dict[str, Dict[int, Dict[str, Union[str, int]]]] = {}

    def execute(self) -> Self:
        (
            self.get_occurrences()
        )
        return self

    def get_occurrences(self):
        for key, pattern in self.patterns.items():
            occurrences = TextParser.find_occurrences(pattern, self.file_path)
            if occurrences:
                self.occurrences.update(
                    {key: occurrences})




