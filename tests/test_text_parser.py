from re import Pattern

from src.chatregex.pipeline import a_study_in_scarlet, the_secret_adversary, the_sign_of_four
import pytest

from src.chatregex.pipeline.text_parser import TextParser
from tests import read_file

@pytest.mark.parametrize('text, expected',
                         [
                             ('Mr. Sherlock Holmes, and Mrs. Anne Walace. Enoch J. Drubber and Mr. Holmes.', 'Sherlock Holmes, and Anne Walace. Enoch Drubber and Holmes.')
                         ])
def test_remove_titles(text, expected):
    # given
    # when
    text = TextParser.remove_titles(text)

    # then
    assert text == expected

@pytest.mark.parametrize('file_path, pattern, expected_chapter_n, expected_sentence_n, expected_sentence, expected_match',
                         [
                            # ('./stubs/a_study_in_scarlet.txt', a_study_in_scarlet['investigator_pattern'], 1, 1, '', 'Sherlock Holmes'),
                            ('./stubs/a_study_in_scarlet.txt', a_study_in_scarlet['crime_pattern'], 1, 1, '', 'Sherlock Holmes'),
                            # ('./stubs/the_sign_of_four.txt', the_sign_of_four['investigator_pattern'], 1, 1, '', ''),
                            # ('./stubs/the_secret_adversary.txt', the_secret_adversary['investigator_pattern'], 1, 1, '', '')
                         ])
def test_find_occurrences(file_path: str, pattern: Pattern, expected_chapter_n: int, expected_sentence_n: int, expected_sentence: str, expected_match: str):
    # given
    text = read_file(file_path)
    text = TextParser.remove_titles(text)

    # when
    occurrence_result = TextParser.find_occurrences(pattern, text)

    # then
    assert occurrence_result[1]['chapter_number'] == expected_chapter_n
    assert occurrence_result[1]['sentence_number'] == expected_sentence_n
    assert occurrence_result[1]['sentence'] == expected_sentence
    assert occurrence_result[1]['match'] == expected_match
