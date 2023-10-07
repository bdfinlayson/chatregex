from re import Pattern
from typing import Self, Dict, Union

from src.chatregex.pipeline.text_parser import TextParser


class Pipeline:
    text: str

    def __int__(self, file_path: str, patterns: Dict[str, Pattern], occurrence_n=1):
        self.file_path = file_path
        self.patterns = patterns
        self.occurrence_n = occurrence_n
        self.occurrences: Dict[str, Dict[int, Dict[str, Union[str, int]]]] = {}

    def execute(self) -> Self:
        (
            self.read_file()
                .clean_text()
                .get_occurrences()
        )
        return self

    def read_file(self) -> Self:
        with open(self.file_path, 'r') as file:
            self.text = file.read()
        return self

    def clean_text(self) -> Self:
        self.text = TextParser.remove_titles(self.text)
        return self

    def get_occurrences(self) -> Self:
        for key, pattern in self.patterns.items():
            occurrences = TextParser.find_occurrences(pattern, self.file_path)
            if occurrences:
                self.occurrences.update(
                    {key: occurrences})
        return self




