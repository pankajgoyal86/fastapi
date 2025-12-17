
import requests
from typing import Any, Dict

BASE_URL = "http://127.0.0.1:8000"
TIMEOUT = 5  # seconds


def get_root() -> Dict[str, Any]:
    """Call GET / and return the JSON response."""
    url = f"{BASE_URL}/"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def get_item_str(item: str) -> Dict[str, Any]:
    """Call GET /items/{item} with a string path parameter."""
    url = f"{BASE_URL}/items/{item}"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def get_item_int(item_id: int) -> Dict[str, Any]:
    """Call GET /item/{item_id} with an integer path parameter."""
    url = f"{BASE_URL}/item/{item_id}"
    resp = requests.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    try:
        print("GET / ->", get_root())
        # print("GET /items/hello ->", get_item_str("hello"))
        # print("GET /item/42 ->", get_item_int(42))
    except requests.HTTPError as e:
        # Server returned a non-2xx response
        print(f"HTTP error: {e.response.status_code} - {e.response.text}")
    except requests.RequestException as e:
        # Network/timeout/connection error
        pass
