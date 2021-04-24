from enum import Enum

import requests

from objectrest import requests as objectrest_requests


class RequestType(Enum):
    GET = 1,
    POST = 2,
    PUT = 3,
    PATCH = 4,
    DELETE = 5


def _filter_params(params: dict = None):
    filtered_params = {}

    if not params:
        return filtered_params

    for k, v in params.items():
        if v is None:
            pass
        else:
            filtered_params[k] = v
    return filtered_params


class RequestHandler:
    def __init__(self, base_url: str, api_key: str, return_objects: bool = False):
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        self._base = base_url
        self._key = api_key
        self._raw = not return_objects

        self._session = requests.Session()

    def _get_headers(self):
        return {'X-API-SECRET': f'{self._key}'}

    def _make_url(self, uri: str):
        if uri.startswith("/"):
            uri = uri[1:]
        return f"{self._base}/{uri}"

    def request(self, request_type: RequestType, uri: str, params: dict = None, model: type = None, data: dict = None):
        url = self._make_url(uri)
        headers = self._get_headers()
        params = _filter_params(params)

        if self._raw:  # raw request
            if request_type == RequestType.GET:
                return objectrest_requests.get_json(url=url, session=self._session, params=params,
                                                    headers=headers)
            if request_type == RequestType.POST:
                return objectrest_requests.post_json(url=url, session=self._session, params=params, data=data,
                                                     headers=headers)
            if request_type == RequestType.PUT:
                return objectrest_requests.put_json(url=url, session=self._session, params=params, data=data,
                                                    headers=headers)
            if request_type == RequestType.PATCH:
                return objectrest_requests.patch_json(url=url, session=self._session, params=params, data=data,
                                                      headers=headers)
            if request_type == RequestType.DELETE:
                return objectrest_requests.delete_json(url=url, session=self._session, params=params, data=data,
                                                       headers=headers)
        else:  # object request
            if request_type == RequestType.GET:
                return objectrest_requests.get_object(url=url, session=self._session, params=params, model=model,
                                                      headers=headers, sub_keys=['data'])
            if request_type == RequestType.POST:
                return objectrest_requests.post_object(url=url, session=self._session, params=params, data=data,
                                                       model=model, headers=headers, sub_keys=['data'])
            if request_type == RequestType.PUT:
                return objectrest_requests.put_object(url=url, session=self._session, params=params, data=data,
                                                      model=model, headers=headers, sub_keys=['data'])
            if request_type == RequestType.PATCH:
                return objectrest_requests.patch_object(url=url, session=self._session, params=params, data=data,
                                                        model=model, headers=headers, sub_keys=['data'])
            if request_type == RequestType.DELETE:
                return objectrest_requests.delete_object(url=url, session=self._session, params=params, data=data,
                                                         model=model, headers=headers, sub_keys=['data'])
