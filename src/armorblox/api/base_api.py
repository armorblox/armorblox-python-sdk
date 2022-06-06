# -*- coding: utf-8 -*-


import requests


class BaseApi:

    def __init__(self, config):
        self._config = config

    @property
    def version(self):
        return 'v1beta1'

    def default_headers(self):
        return {
            'X-Ab-Authorization': self._config.api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'Armorblox-Python-SDK/' + self._config.sdk_version
        }

    def endpoint(self, path: str, api_version: str = None) -> str:
        if api_version is None:
            api_version = self.version
        return self._config.base_api_url.format(api_version) + path

    def list_resource(self, path: str, headers: dict = None,
                      params: dict = None, options: dict = None):
        """

        Args:
            path: str
            headers: dict
            params: dict
            options: dict

        Raises:
            Exception:
        """
        if options is None:
            options = {}
        response = requests.get(self.endpoint(path, options.get('api_version')),
                                headers=self.default_headers(), params=params)
        if response.status_code == 200:
            response_json = response.json()
            next_page_token = response_json.get('next_page_token', None)
            return response_json.get('incidents', [])
        else:
            return []
    
    def read_resource(self, path: str, incident_id: int, headers: dict = None,
                      params: dict = None, options: dict = None):
        
        if options is None:
            options = {}
            
        url = self.endpoint(path, options.get('api_version')) + f"/{incident_id}"
        
        response = requests.get(url,headers=self.default_headers(), params=params)
        
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            return {}


