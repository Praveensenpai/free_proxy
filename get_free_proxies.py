import requests
from typing import Iterator


def get_free_proxies() -> Iterator:
    data = requests.get(
        "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc").json()

    return (i["ip"] for i in data["data"])
