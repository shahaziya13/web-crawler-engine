from collections import Counter
import re


class KeywordFrequency:
    def analyze(self, pages: list, top_n: int = 10):
        counter = Counter()

        for page in pages:
            text = " ".join(page["paragraphs"]).lower()

            words = re.findall(r"\b[a-zA-Z]{3,}\b", text)

            counter.update(words)

        return counter.most_common(top_n)