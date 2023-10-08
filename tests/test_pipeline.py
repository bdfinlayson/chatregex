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
                                 'sentence_number': 41}
                              )
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
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'investigator', "The investigator's appearance for the 1st time is in chapter #1 and sentence #41. The investigator is Sherlock Holmes."),
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'perpetrator', "The perpetrator's appearance for the 1st time is in chapter #7 and sentence #186. The perpetrator is Jefferson Hope."),
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'crime', "The crime's appearance for the 1st time is in chapter #3 and sentence #35. The crime is described as follows:  He found the door open, and in the front room, which is bare of furniture, discovered the body of a gentleman, well dressed, and having cards in his pocket bearing the name of ‘Enoch Drebber, Cleveland, Ohio,S.."),
                             (a_study_in_scarlet_path, a_study_in_scarlet, 'suspects', 'The suspects Joseph Stangerson, Arthur Charpentier make appearances for the 1st time in chapters 3, 6 and in sentences 182, 71, respectively.'),
                         ])
def test_pipeline_answer(file_path: str, patterns: Dict[str, Pattern], subject: str, expected: str):
    # given
    pipeline = Pipeline().build(file_path, patterns)

    # when
    pipeline.execute()

    # then
    assert pipeline.answers[subject] == expected