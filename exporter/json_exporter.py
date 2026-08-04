import json
import os


class JSONExporter:
    def export(self, data: list, filename: str = "data/output.json"):
        os.makedirs("data", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)