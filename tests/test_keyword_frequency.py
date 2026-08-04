from parser.keyword_frequency import KeywordFrequency


def test_frequency():
    pages = [
        {
            "paragraphs": [
                "Python Python crawler crawler crawler"
            ]
        }
    ]

    frequency = KeywordFrequency()

    result = frequency.analyze(pages)

    assert result[0][0] == "crawler"
    assert result[0][1] == 3