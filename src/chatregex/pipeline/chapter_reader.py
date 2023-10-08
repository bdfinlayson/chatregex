import re


class ChapterReader:
    @staticmethod
    def split_by_chapter(text: str) -> list[str]:
        chapters = re.split(r'\n\n\nchapter', text, flags=re.IGNORECASE)[1:]
        return chapters

    @staticmethod
    def split_by_paragraph(text: str) -> list[str]:
        paragraph_marker = '###########'
        text = text.replace('\n\n', paragraph_marker).replace('\n', ' ')
        paragraphs = text.split(paragraph_marker)
        try:
            paragraphs.remove("")
        except ValueError:
            pass
        return paragraphs

    @staticmethod
    def split_by_sentence(text: str) -> list[str]:
        sentences = re.findall(r'[^.!?]+[.!?]', text)
        return sentences
