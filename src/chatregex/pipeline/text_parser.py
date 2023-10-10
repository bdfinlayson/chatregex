import re
from typing import Dict, Union

from .chapter_reader import ChapterReader
from re import Pattern


class TextParser:
    stop_words = {'hello', 'goodbye', 'yet', 'would', 'said', 'if', 'project', 'gutenberg', 'what', 'yes', 'no', 'that', 'then', 'my', 'in', 'and', 'we', 'you', 'there', 'the', 'sir', 'he', 'she', 'him', 'her', 'to', 'it', 'but', 'since', 'well', 'how', 'let', 'just', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"}

    @staticmethod
    def remove_honorific(text: str):
        pattern = re.compile(r'dr\.|st\.|mr\.|mrs\.|ms\.|\s\w\.', flags=re.IGNORECASE)
        text = re.sub(pattern, '', text)
        text = re.sub(r'  ', ' ', text)
        text = text.strip()
        return text

    @staticmethod
    def find_occurrences(pattern: Pattern, text: str) -> Dict[int, Dict[str, Union[str, int, list[str]]]]:
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
                                'match': match.group(),
                                'surrounding_words': TextParser.get_surrounding_words(match.group(), sentence)
                            }
                        }
                    )

        return occurrences

    @staticmethod
    def get_surrounding_words(match: str, text: str, window: int = 3) -> list[str]:
        # clean text of punctuation
        text = re.sub(r'\W', ' ', text, flags=re.IGNORECASE).replace('  ', ' ')
        # remove noise words
        text = ' '.join(list(filter(lambda word: word.lower() not in TextParser.stop_words, text.split())))

        surrounding_words = []
        segments = text.split(match)
        for idx, segment in enumerate(segments):
            if idx == 0:
                before = segment.split()[-window:]
                surrounding_words += before
            elif idx != len(segments) - 1:
                before = segment.split()[-window:]
                after = segment.split()[:window]
                surrounding_words += before
                surrounding_words += after
            else:
                after = segment.split()[:window]
                surrounding_words += after

        # normalize words
        surrounding_words = [word.lower() for word in surrounding_words]

        return surrounding_words

    @staticmethod
    def build_bag_of_words():
        pass



