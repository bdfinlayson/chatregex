import re


class ChapterReader:
    @staticmethod
    def split_by_chapter(text: str) -> list[str]:
        chapters = re.split(r'\n\n\nchapter.*\n.*\n', text, flags=re.IGNORECASE)[1:]
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
        # Preserve strings like "H. W. McGee" or "Dr. Watson"
        # In other words, these periods are swapped with some token '@' 
        # so that they aren't interpreted as sentence terminators
        text = re.sub(r"(?:(?<=[A-Z])|(?<=Mrs)|(?<=Mr)|(?<=Ms)|(?<=Dr)|(?<=St))\.( )?", r'@\1', text)
        sentences = re.findall(r'[^.!?]+[.!?]', text)
        for i in range(len(sentences)):
            sentence = sentences[i]
            #sentences[i] = re.sub(r"@", r'.', sentence)
        return sentences
