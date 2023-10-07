import re
from typing import Dict, Union

from src.chatregex.pipeline.chapter_reader import ChapterReader
from re import Pattern


class TextParser:
    @staticmethod
    def remove_titles(text: str):
        pattern = re.compile(r'dr\.|st\.|mr\.|mrs\.|ms\.|\s\w\.', flags=re.IGNORECASE)
        text = re.sub(pattern, '', text)
        text = re.sub(r'  ', ' ', text)
        text = text.strip()
        return text

    @staticmethod
    def find_occurrences(pattern: Pattern, text: str) -> Dict[int, Dict[str, Union[str, int]]]:
        occurence_n = 0
        occurrences = {}

        chapters = ChapterReader.split_by_chapter(text)

        for idx, chapter in enumerate(chapters):
            chapter_n = idx + 1
            text = ' '.join(ChapterReader.split_by_paragraph(chapter))

            for idx2, sentence in enumerate(ChapterReader.split_by_sentence(text)):
                sentence_n = idx2 + 1
                match = re.search(pattern, sentence)
                if bool(match):
                    occurence_n += 1
                    occurrences.update(
                        {
                            occurence_n: {
                                'chapter_number': chapter_n,
                                'sentence_number': sentence_n,
                                'sentence': sentence,
                                'match': match.group()
                            }
                        }
                    )

        return occurrences



