# -*- coding: utf-8 -*-


from armorblox.api.base_api import BaseApi


class IncidentsApi(BaseApi):
    PATH = 'incidents'
    PAGE_SIZE = 100
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def __init__(self, config):
        super().__init__(config)

    def list(self):
        #            "from_date": "",
        #            "to_date": "",
        # ABUSE_INCIDENT_TYPE
        # DLP_INCIDENT_TYPE

        # params to pass if incident_id is specified
        if self._config.incident_id:

            params = {
                'pageSize': 1,
                'pageToken': 1
            }

        else:
            params = {
            'page_size': self.PAGE_SIZE,
            'page_token': 0,
            'incidentTypesFilter': 'THREAT_INCIDENT_TYPE',
            'orderBy': 'DESC',
            'sortBy': 'DATE',
            'timeFilter': 'allTime'
        }

        return self.list_resource(self.PATH, params=params)