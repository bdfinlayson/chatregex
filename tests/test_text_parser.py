from re import Pattern

from src.chatregex.pipeline import a_study_in_scarlet, the_secret_adversary, the_sign_of_four
import pytest

from src.chatregex.pipeline.text_parser import TextParser
from tests import read_file, a_study_in_scarlet_path, the_secret_adversary_path, the_sign_of_four_path


@pytest.mark.parametrize('text, expected',
                         [
                             ('Mr. Sherlock Holmes, and Mrs. Anne Walace. Enoch J. Drubber and Mr. Holmes.', 'Sherlock Holmes, and Anne Walace. Enoch Drubber and Holmes.')
                         ])
def test_remove_titles(text, expected):
    # given
    # when
    text = TextParser.remove_honorific(text)

    # then
    assert text == expected


@pytest.mark.parametrize('file_path, pattern, expected_chapter_n, expected_sentence_n, expected_sentence, expected_match, expected_surrounding_words',
                         [
                            (a_study_in_scarlet_path, a_study_in_scarlet['investigator_pattern'], 1, 41, ' “You don’t know Sherlock Holmes yet,” he said; “perhaps you would not care for him as a constant companion.', 'Sherlock Holmes', ['know', 'perhaps', 'care', 'constant']),
                            (a_study_in_scarlet_path, a_study_in_scarlet['crime_pattern'], 3, 35, " He found the door open, and in the front room, which is bare of furniture, discovered the body of a gentleman, well dressed, and having cards in his pocket bearing the name of ‘Enoch Drebber, Cleveland, Ohio,S.", 'Enoch Drebber', ['pocket', 'bearing', 'name', 'cleveland', 'ohio']),
                            (the_secret_adversary_path, the_secret_adversary['investigator_pattern'], 1, 2, ' “TOMMY, old thing!', 'TOMMY', ['old', 'thing']),
                            (the_secret_adversary_path, the_secret_adversary['perpetrator_pattern'], 2, 237,  ' “That’ll do, Brown.', 'Brown', []),
                            (the_secret_adversary_path, the_secret_adversary['suspects_pattern'], 6, 194, ' “We had her down as Rita Vandemeyer, but I suppose that’s incorrect?', 'Rita Vandemeyer', ['suppose', 'incorrect']),
                            (the_secret_adversary_path, the_secret_adversary['crime_pattern'], 4, 185, ' The disappearance of Jane Finn was forgotten and the whole affair was lost in oblivion.', 'disappearance of Jane Finn', ['affair', 'lost', 'oblivion']),
                            (the_sign_of_four_path, the_sign_of_four['investigator_pattern'], 1, 1, ' I The Science of Deduction  Sherlock Holmes took his bottle from the corner of the mantel-piece and his hypodermic syringe from its neat morocco case.', 'Sherlock Holmes', ['science', 'deduction', 'took', 'bottle', 'corner']),
                            (the_sign_of_four_path, the_sign_of_four['perpetrator_pattern'], 3, 54, ' Beside it is written, in very rough and coarse characters, ‘The sign of the four,—Jonathan Small, Mahomet Singh, Abdullah Khan, Dost Akbar.', 'Jonathan Small', ['characters', 'sign', 'four', 'mahomet', 'singh', 'abdullah']),
                            (the_sign_of_four_path, the_sign_of_four['crime_pattern'], 6, 123, ' On getting into the room I at once looked for the means by which the poison had entered the system.', ' poison ', ['room', 'looked', 'means', 'entered', 'system']),
                         ])
def test_find_occurrences(file_path: str, pattern: Pattern, expected_chapter_n: int, expected_sentence_n: int, expected_sentence: str, expected_match: str, expected_surrounding_words: list[str]):
    # given
    text = read_file(file_path)
    text = TextParser.remove_honorific(text)

    # when
    occurrence_result = TextParser.find_occurrences(pattern, text)

    # then
    assert occurrence_result[1]['chapter_number'] == expected_chapter_n
    assert occurrence_result[1]['sentence_number'] == expected_sentence_n
    assert occurrence_result[1]['sentence'] == expected_sentence
    assert occurrence_result[1]['match'] == expected_match
    assert occurrence_result[1]['surrounding_words'] == expected_surrounding_words

@pytest.mark.parametrize('text, match, expected',
                         [
                             ("Hello to you all, my dear friend Sherlock Holmes, and I, investigate crimes in London.", 'Sherlock Holmes', ['dear', 'friend', 'investigate', 'crimes', 'london']),
                             ("Sherlock Holmes, and I, investigate crimes in London.", 'Sherlock Holmes', ['investigate', 'crimes', 'london']),
                             ("Hello to you all, my dear friend Sherlock Holmes.", 'Sherlock Holmes', ['dear', 'friend']),
                             ("Hello to you all, my dear friend Sherlock Holmes, in London the weather is good, Sherlock Holmes the detective.", 'Sherlock Holmes', ['dear', 'friend', 'london', 'weather', 'good', 'london', 'weather', 'good', 'detective']),
                         ])
def test_extract_surrounding_words(text: str, match: str, expected):
    # given
    # when
    result = TextParser.get_surrounding_words(match, text)

    # then
    assert result == expected
