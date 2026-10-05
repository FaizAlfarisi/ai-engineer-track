import pytest

import local_api
import sess_client


@pytest.fixture
def api():
    server = local_api.LocalAPI()
    yield server
    server.stop()


def test_session_carries_auth_header_once():
    sess = sess_client.make_session("k-1")
    try:
        assert sess.headers.get("Authorization") == "Bearer k-1"
    finally:
        sess.close()


def test_fetch_items_via_session(api):
    sess = sess_client.make_session("k-1")
    try:
        data = sess_client.fetch_with(sess, api.base, "/items")
        assert data["count"] == 4
    finally:
        sess.close()


def test_fetch_404_raises_with_status(api):
    sess = sess_client.make_session("k-1")
    try:
        with pytest.raises(sess_client.ShopError) as exc:
            sess_client.fetch_with(sess, api.base, "/items/999")
        assert exc.value.status == 404
    finally:
        sess.close()
