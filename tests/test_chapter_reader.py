import pytest

from src.chatregex.pipeline.chapter_reader import ChapterReader
from tests import read_file


@pytest.mark.parametrize(
    'file_path, expected_number_of_chapters',
    [
        ('./stubs/a_study_in_scarlet.txt', 14),
        ('./stubs/the_sign_of_four.txt', 12),
        ('./stubs/the_secret_adversary.txt', 28)
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
        ('./stubs/a_study_in_scarlet.txt', [70]),
        ('./stubs/the_sign_of_four.txt', [56]),
        ('./stubs/the_secret_adversary.txt', [118])
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
        ('./stubs/a_study_in_scarlet.txt', [5]),
        ('./stubs/the_sign_of_four.txt', [4]),
        ('./stubs/the_secret_adversary.txt', [1])
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

