import re


class ChapterReader:
    def split_by_chapter(self, file_path: str):
        with open(file_path, 'r') as file:
            text = file.read()
            chapters = text.lower().split('\n\n\nchapter')[1:]
            return chapters

    def split_by_paragraph(self, text: str):
        paragraph_marker = '###########'
        text = text.replace('\n\n', paragraph_marker).replace('\n', ' ')
        paragraphs = text.split(paragraph_marker)
        try:
            paragraphs.remove("")
        except ValueError:
            pass
        return paragraphs

    def split_by_sentence(self, text: str):
        sentences = re.findall(r'[^.!?]+[.!?]', text)
        return sentences
