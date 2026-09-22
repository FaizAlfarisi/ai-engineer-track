"""Weather client for Lesson 18 — H1 debug drill.

Four bugs are planted in this file. Find and fix all four so
`python -m pytest test_weather.py -q` reports 4 passed.

Do NOT touch test_weather.py or local_api.py. Run the Debugging
Protocol for each failure and fill the four rows of the H1 bug report
table as you go.
"""

import json
import urllib.error
import urllib.request
from urllib.parse import urlencode


class WeatherError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.message = message
        self.status = status


def _request(base: str, city: str) -> dict:
    query = urlencode({"city": city})
    url = base + "/weather?" + query
    try:
        with urllib.request.urlopen(url, timeout=3) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            return payload
    except urllib.error.HTTPError as exc:
        raise WeatherError(f"http {exc.code}", status=exc.code) from exc
    except urllib.error.URLError as exc:
        raise WeatherError(f"network error: {exc.reason}") from exc
    except TimeoutError as exc:
        raise WeatherError(f"timeout: {exc}") from exc


def get_weather(base: str, city: str) -> dict:
    payload = _request(base, city)
    return {
        "condition": payload["condition"],
        "temp_c": payload["temp_c"],
    }