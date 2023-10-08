import pytest

from src.chatregex.pipeline.chapter_reader import ChapterReader
from tests import read_file, a_study_in_scarlet_path, the_sign_of_four_path, the_secret_adversary_path


@pytest.mark.parametrize(
    'file_path, expected_number_of_chapters',
    [
        (a_study_in_scarlet_path, 14),
        (the_sign_of_four_path, 12),
        (the_secret_adversary_path, 28)
    ]
)
def test_split_by_chapter(file_path, expected_number_of_chapters):
    # given
    text = read_file(file_path)

    # when
    chapters = ChapterReader.split_by_chapter(text)

    # then
    assert len(chapters) == expected_number_of_chapters


@pytest.mark.parametrize(
    'file_path, expected_number_of_chapter_paragraphs',
    [
        (a_study_in_scarlet_path, [70]),
        (the_sign_of_four_path, [56]),
        (the_secret_adversary_path, [118])
    ]
)
def test_split_by_paragraph(file_path, expected_number_of_chapter_paragraphs):
    # given
    text = read_file(file_path)

    # when
    chapters = ChapterReader.split_by_chapter(text)

    # then
    assert len(ChapterReader.split_by_paragraph(chapters[0])) == expected_number_of_chapter_paragraphs[0]


@pytest.mark.parametrize(
    'file_path, expected_number_of_chapter_sentences',
    [
        (a_study_in_scarlet_path, [5]),
        (the_sign_of_four_path, [4]),
        (the_secret_adversary_path, [1])
    ]
)
def test_split_by_sentence(file_path, expected_number_of_chapter_sentences):
    # given
    text = read_file(file_path)

    # when
    chapters = ChapterReader.split_by_chapter(text)
    paragraphs = ChapterReader.split_by_paragraph(chapters[0])

    # then
    assert len(ChapterReader.split_by_sentence(paragraphs[1])) == expected_number_of_chapter_sentences[0]

