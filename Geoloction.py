from functools import lru_cache
from typing import Any
import requests 
from dataclasses import dataclass
@dataclass
class GeoData:
    ip: str
    city:str
    region:str
    country:str
    loc:str
    org:str
    postal:str
    timezone:str
    hostname:str
    readme:str

class Geoloction:
    def __init__(self) -> None:
        pass 

    @lru_cache()
    def get_location(self) -> GeoData:
        """
        This will make a request to ipinfo.io and Return GeoData Object this will also use a Cache
        Returns:
            GeoData: _description_
        """
        request_json:Any = requests.get(url="https://ipinfo.io").json()
        return GeoData(**request_json)




if __name__ == "__main__":
    print(Geoloction().get_location())