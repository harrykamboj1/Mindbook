import requests


class ScrapeDoClient:
    def __init__(self, api_key: str, base_url: str = "https://api.scrape.do/"):
        self.api_key = api_key
        self.base_url = base_url

    def get(self, url: str, render: bool = False, **kwargs):
        params = {
            "token": self.api_key,
            "url": url,
        }

        if render:
            params["render"] = "true"

        params.update(kwargs)

        response = requests.get(self.base_url, params=params, timeout=60)
        response.raise_for_status()
        return response