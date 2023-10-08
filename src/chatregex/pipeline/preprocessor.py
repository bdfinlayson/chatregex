import re


class Preprocessor:
    stop_words = {'if', 'project', 'gutenberg', 'what', 'yes', 'no', 'that', 'then', 'my', 'in', 'and', 'we', 'you', 'there', 'the', 'sir', 'he', 'she', 'him', 'her', 'to', 'it', 'but', 'since', 'well', 'how', 'let', 'just'}
    names_pattern = r'(?![.!?“”,])?\b([A-Z]\w+)\b(?![.])'

    def process(self, text: str):
        """TODO"""

    def get_protagonist_name(self, text: str):
        return self.get_top_n_character_names(1, text)[0]

    def get_top_n_character_names(self, n: int, text: str):
        bow = self.find_all(self.names_pattern, text)
        top_items = sorted(bow.items(), key=lambda item: item[1], reverse=True)[:n]
        return [name[0] for name in top_items]

    def find_all(self, pattern: str, text):
        raw_matches = re.findall(pattern, text)
        target_words = filter(lambda word: word.lower() not in self.stop_words, raw_matches)
        bow = {word: list(raw_matches).count(word) for word in list(target_words)}
        return bow
