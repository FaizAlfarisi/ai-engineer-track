import pytest
from store_client import StoreError, create_item, get_item, list_items
from store_server import StoreAPI


@pytest.fixture
def api():
    with StoreAPI() as server:
        yield server.base


def test_happy_path(api):
    created = create_item(api, name="espresso", price=3.0)
    assert created["id"] == 1
    assert created["name"] == "espresso"
    assert created["price"] == 3.0

    items = list_items(api)
    assert len(items) == 1
    assert items[0]["name"] == "espresso"

    item = get_item(api, 1)
    assert item["name"] == "espresso"


def test_post_validation(api):
    with pytest.raises(StoreError) as exc_info:
        create_item(api, name="", price=2.5)
    assert exc_info.value.status == 400

    with pytest.raises(StoreError) as exc_info:
        create_item(api, name="cookie", price=-1.0)
    assert exc_info.value.status == 400


def test_missing_item(api):
    with pytest.raises(StoreError) as exc_info:
        get_item(api, 999)
    assert exc_info.value.status == 404