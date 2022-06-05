# -*- coding: utf-8 -*-


from armorblox.config import Config
from armorblox.api.incidents_api import IncidentsApi
from cached_property import cached_property


class Client:

    @staticmethod
    def sdk_version():
        return '0.1.0.20220201'

    def __init__(self, api_key: str, instance_name: str = None, instance_url: str = None):
        self.config = Config(api_key,
                             instance_name=instance_name,
                             instance_url=instance_url,
                             sdk_version=self.sdk_version())

    @cached_property
    def incidents(self):
        return IncidentsApi(self.config)
