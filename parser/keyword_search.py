from typing import List


class KeywordSearch:
    def search(self, pages: List[dict], keyword: str) -> List[dict]:
        keyword = keyword.lower()
        matches = []

        for page in pages:
            text = " ".join(page["paragraphs"]).lower()

            if keyword in text:
                matches.append(page)

        return matches