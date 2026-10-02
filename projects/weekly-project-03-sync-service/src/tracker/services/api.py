import requests
import logging
import stub_api
from src.shared.utils.exceptions import ApiError
logger = logging.getLogger(__name__)

def get_items():
    api = stub_api.StubAPI()
    logger.info("server started: %s", api.base)

    try:
        response = requests.get(
            f"{api.base}/items",
            timeout=30,
        )
        response.raise_for_status()
    except requests.HTTPError as exc:
        code = exc.response.status_code
        logger.error("API error: http %d", code)
        raise ApiError(message=f"http {code}", status=code) from exc
    except requests.ConnectionError as exc:
        logger.error("API error: network error: %s", exc)
        raise ApiError(message=f"network error: {exc}") from exc
    except requests.Timeout as exc:
        logger.error("API error: timeout: %s", exc)
        raise ApiError(message=f"timeout: {exc}") from exc
    except requests.RequestException:
        logger.error("API error: unexpected error")
        raise ApiError(message=f"unexpected error")
    finally:
        api.stop()
        
    network = response.json().get("items", [])
    logger.debug("fetched data from api: %s", network)
    return network