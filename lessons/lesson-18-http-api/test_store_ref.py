"""Reference test for the spec-faithful server (`store_server_ref`).

Reuses the same `store_client.py` interface as your `test_store.py`, so
running both suites together verifies the two server designs are drop-in
compatible — same client, either server.

Run:
    pytest test_store.py test_store_ref.py
"""

import threading

import pytest

import store_server_ref
from store_client import StoreError, create_item, get_item, list_items


@pytest.fixture
def store():
    server = store_server_ref.start()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_address[1]}"
    yield base
    server.shutdown()
    server.server_close()


def test_create_then_list(store):
    created = create_item(store, "cookie", 1.25)
    assert created["id"] == 1
    assert created["price"] == 1.25
    assert list_items(store)[0]["name"] == "cookie"


def test_create_validates_payload(store):
    with pytest.raises(StoreError) as exc:
        create_item(store, "", -5)
    assert exc.value.status == 400


def test_get_missing_raises_404(store):
    with pytest.raises(StoreError) as exc:
        get_item(store, 999)
    assert exc.value.status == 404