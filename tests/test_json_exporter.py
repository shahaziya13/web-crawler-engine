import os

from exporter.json_exporter import JSONExporter


def test_json_export(tmp_path):
    file = tmp_path / "test.json"

    exporter = JSONExporter()

    exporter.export(
        [{"title": "Example"}],
        str(file)
    )

    assert os.path.exists(file)