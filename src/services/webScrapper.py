from src.services.scrapedo_client import ScrapeDoClient
from src.config.index import appConfig

scrapedo_client = ScrapeDoClient(api_key=appConfig["scraping_do_api_key"])