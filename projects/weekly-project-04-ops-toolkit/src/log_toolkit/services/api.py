import os

import requests
import logging
import stub_feed
from src.utils.exceptions import ApiError
logger = logging.getLogger(__name__)

def get_incident():
    override = os.environ.get("FEED_API_BASE")
    api = None
    if override:
        base = override
        logger.info("using API base from FEED_API_BASE: %s", base)
    else:
        api = stub_feed.StubAPI()
        base = api.base
        logger.info("server started: %s", base)

    try:
        response = requests.get(
            f"{base}/incident",
            timeout=30,
        )
        response.raise_for_status()
    except requests.HTTPError as exc:
        code = exc.response.status_code
        logger.error("API error: http %d", code)
        raise ApiError(message=f"http {code}", status=code) from exc
    except requests.ConnectionError as exc:
        logger.error("API error: network error: %s", exc)
        raise ApiError(message=f"{exc}") from exc
    except requests.Timeout as exc:
        logger.error("API error: timeout: %s", exc)
        raise ApiError(message=f"timeout: {exc}") from exc
    except requests.RequestException:
        logger.error("API error: unexpected error")
        raise ApiError(message=f"unexpected error")
    finally:
        if api is not None:
            api.stop()
        
    network = response.json()
    logger.debug("fetched data from api: %s", network)
    return network