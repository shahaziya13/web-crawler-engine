import os
import pandas as pd


class CSVExporter:
    def export(self, data: list, filename: str = "data/output.csv"):
        os.makedirs("data", exist_ok=True)

        rows = []

        for page in data:
            rows.append({
                "Title": page["title"],
                "Headings": " | ".join(page["headings"]),
                "Paragraph Count": len(page["paragraphs"]),
                "Links": len(page["links"]),
                "Images": len(page["images"])
            })

        dataframe = pd.DataFrame(rows)
        dataframe.to_csv(filename, index=False)