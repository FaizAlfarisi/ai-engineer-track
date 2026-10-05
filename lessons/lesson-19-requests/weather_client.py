"""Weather client for Lesson 19 — H1 debug drill.

Four bugs are planted in this file. Find and fix all four so
`python -m pytest test_weather.py -q` reports 4 passed.

Do NOT touch test_weather.py or local_api.py. Run the Debugging
Protocol for each failure and fill the four rows of the H1 bug report
table as you go.
"""

import requests


class WeatherError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.message = message
        self.status = status


def _request(base: str, city: str) -> dict:
    try:
        resp = requests.get(base + "/weather", params={"city": city}, timeout=3)
        resp.raise_for_status()
        return resp.json()
        
    except requests.HTTPError as exc:
        raise WeatherError(
            f"http {exc.response.status_code}",
            status=exc.response.status_code,
        ) from exc
    except requests.RequestException as exc:
        raise WeatherError(f"network error: {exc}") from exc

def get_weather(base: str, city: str) -> dict:
    payload = _request(base, city)
    return {
        "condition": payload["condition"],
        "temp_c": payload["temp_c"],
    }
