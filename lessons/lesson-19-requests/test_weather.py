import pytest

import local_api
import weather_client


@pytest.fixture
def api():
    server = local_api.LocalAPI()
    yield server
    server.stop()


def test_get_weather_parses_json(api):
    report = weather_client.get_weather(api.base, "tokyo")
    assert report == {"condition": "sunny", "temp_c": 24.5}


def test_get_weather_city_with_space(api):
    report = weather_client.get_weather(api.base, "new york")
    assert report == {"condition": "foggy", "temp_c": 18.2}


def test_unknown_city_raises_http_error_status(api):
    with pytest.raises(weather_client.WeatherError) as exc:
        weather_client.get_weather(api.base, "atlantis")
    assert exc.value.status == 404


def test_no_network_is_not_confused_with_http(api):
    with pytest.raises(weather_client.WeatherError) as exc:
        weather_client.get_weather("http://127.0.0.1:1", "tokyo")
    assert exc.value.status is None
