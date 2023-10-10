from re import Pattern
from typing import Dict, Union

import pytest

from src.chatregex.pipeline import a_study_in_scarlet
from src.chatregex.pipeline.pipeline import Pipeline
from tests import a_study_in_scarlet_path


@pytest.mark.parametrize('file_path, patterns, subject, expected',
                         [
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'investigator', {
                                 'chapter_number': 1,
                                 'match': 'Sherlock Holmes',
                                 'sentence': ' “You don’t know Sherlock Holmes yet,” he said; “perhaps you would not care for him as a constant companion.',
                                 'sentence_number': 41,
                                 'surrounding_words': ['know', 'perhaps', 'care', 'constant']
                             })
                         ])
def test_pipeline_execute(file_path: str, patterns: Dict[str, Pattern], subject: str, expected: Dict[str, Union[int, str]]):
    # given
    pipeline = Pipeline().build(file_path, patterns)

    # when
    pipeline.execute()

    # then
    assert pipeline.occurrences[subject][1] == expected


@pytest.mark.parametrize('file_path, patterns, subject, expected',
                         [
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'investigator', "The investigator's appearance for the 1st time is in chapter #1 and sentence #41. The investigator is Sherlock Holmes and appears 48 times in the book. The most common words surrounding \"Sherlock Holmes\" are: sprang (3 times), know (2 times), rose (2 times)."),
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'perpetrator', "The perpetrator's appearance for the 1st time is in chapter #7 and sentence #186. The perpetrator is Jefferson Hope and appears 35 times in the book. The most common words surrounding \"Jefferson Hope\" are: among (3 times), led (3 times), able (2 times)."),
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'crime', "The crime's appearance for the 1st time is in chapter #3 and sentence #35. Overall, the crime is mentioned 9 times. The crime is described as follows:  He found the door open, and in the front room, which is bare of furniture, discovered the body of a gentleman, well dressed, and having cards in his pocket bearing the name of ‘Enoch Drebber, Cleveland, Ohio,S.. The most common words surrounding \"Enoch Drebber\" are: cleveland (4 times), hope (2 times), joseph (2 times)."),
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'suspects', 'The suspects Joseph Stangerson, Arthur Charpentier make appearances for the 1st time in chapters 3, 6 and in sentences 182, 71, respectively. Overall, the suspects appear Joseph Stangerson appears 10 times and Arthur Charpentier appears 1 times. The most common words surrounding "Joseph Stangerson" are: drebber (4 times), secretary (3 times), name (2 times). The most common words surrounding "Arthur Charpentier" are: sub (1 times), lieutenant (1 times), majesty (1 times).'),
                         ])
def test_pipeline_answer(file_path: str, patterns: Dict[str, Pattern], subject: str, expected: str):
    # given
    pipeline = Pipeline().build(file_path, patterns)

    # when
    pipeline.execute()

    # then
    assert pipeline.answers[subject] == expected

@pytest.mark.parametrize('occurrences, expected',
                         [
                             ({
                                  1: {'match': 'test', 'surrounding_words': ['one', 'two', 'three']},
                                  2: {'match': 'test', 'surrounding_words': ['two', 'three', 'three', 'four']},
                                  3: {'match': 'foo', 'surrounding_words': ['two', 'three', 'three', 'four']}
                              },
                              'The most common words surrounding "test" are: three (3 times), two (2 times), one (1 times)'
                             )
                         ])
def test_build_common_surrounding_words(occurrences: Dict[int, Dict[str, list[str]]], expected: str):
    # given
    pipeline = Pipeline()

    # when
    result = pipeline.build_common_surrounding_words_answer('test', occurrences)

    # then
    assert result == expected
