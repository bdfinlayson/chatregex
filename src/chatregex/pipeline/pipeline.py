import os
from re import Pattern
from typing import Dict, Union

from .text_parser import TextParser


class Pipeline:
    text: str
    file_path: str
    patterns: Dict[str, Pattern]
    occurrence_n: int
    occurrences: Dict[str, Dict[int, Dict[str, Union[str, int]]]]
    answers: Dict[str, str]

    def build(self, file_path: str, patterns: Dict[str, Pattern], occurrence_n=1) -> "Pipeline":
        self.file_path = file_path
        self.patterns = patterns
        self.occurrence_n = occurrence_n
        self.occurrences = {}
        self.answers = {}
        return self

    def execute(self) -> "Pipeline":
        (
            self.read_file()
                .clean_text()
                .get_occurrences()
                .build_answers()
        )
        return self

    def read_file(self) -> "Pipeline":
        with open(self.file_path, 'r') as file:
            self.text = file.read()
        return self

    def clean_text(self) -> "Pipeline":
        self.text = TextParser.remove_titles(self.text)
        return self

    def get_occurrences(self) -> "Pipeline":
        for key, pattern in self.patterns.items():
            human_readable_key = key.replace('_pattern', '')
            occurrences = TextParser.find_occurrences(pattern, self.text)
            if occurrences:
                self.occurrences.update({human_readable_key: occurrences})
        return self

    def build_answers(self) -> "Pipeline":
        self.answers = {
            'investigator': self.build_answer('investigator'),
            'perpetrator': self.build_answer('perpetrator'),
            'crime': self.build_crime_answer(),
            'suspects': self.build_suspects_answer()
        }
        return self

    def build_answer(self, subject: str) -> str:
        o = self.occurrences[subject][self.occurrence_n]
        return f"The {subject}'s appearance for the {self.occurrence_n}{self.cardinal_number_suffix()} time is in chapter #{o['chapter_number']} and sentence #{o['sentence_number']}. The {subject} is {o['match'].title()}."

    def build_crime_answer(self) -> str:
        o = self.occurrences['crime'][self.occurrence_n]
        return f"The crime's appearance for the {self.occurrence_n}{self.cardinal_number_suffix()} time is in chapter #{o['chapter_number']} and sentence #{o['sentence_number']}. The crime is described as follows: {o['sentence']}."

    def build_suspects_answer(self) -> str:
        o = self.occurrences['suspects']
        suspects = {}
        for k, v in o.items():
            if v['match'] not in suspects:
                suspects.update({v['match']: v})

        plural = ''
        if len(suspects) > 1:
            plural = 's'

        names = f"{', '.join(suspects.keys())}"
        chapter_numbers = []
        sentence_numbers = []
        for k, v in suspects.items():
            chapter_numbers.append(str(v['chapter_number']))
            sentence_numbers.append(str(v['sentence_number']))

        chapters = f"{', '.join(chapter_numbers)}"
        sentences = f"{', '.join(sentence_numbers)}"

        return f'The suspect{plural} {names} make appearance{plural} for the {self.occurrence_n}{self.cardinal_number_suffix()} time in chapter{plural} {chapters} and in sentence{plural} {sentences}, respectively.'







    def cardinal_number_suffix(self) -> str:
        if self.occurrence_n == 1:
            return 'st'
        elif self.occurrence_n == 2:
            return 'nd'
        elif self.occurrence_n == 3:
            return 'rd'
        else:
            return 'th'






