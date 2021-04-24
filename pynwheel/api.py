import warnings
from typing import Union, List

from pynwheel import utils
from pynwheel.enums import *
from pynwheel.request_handler import RequestHandler, RequestType
from pynwheel.models import *


class APIType(Enum):
    SANDBOX = 1,
    DEVELOPMENT = 2,
    PRODUCTION = 3


def get_endpoint(api_type: APIType):
    if api_type == APIType.SANDBOX:
        return "https://sandbox.getpinwheel.com/v1"
    if api_type == APIType.PRODUCTION:
        return "https://api.getpinwheel.com/v1"
    if api_type == APIType.DEVELOPMENT:
        return "https://development.getpinwheel.com/v1"
    raise Exception("Invalid api_type")


class API:
    def __init__(self, api_type: APIType, api_key: str, raw: bool = False):
        raw = True
        warnings.warn('Object creation not supported yet.')

        self._request_handler = RequestHandler(api_key=api_key,
                                               base_url=get_endpoint(api_type=api_type),
                                               return_objects=not raw)

    def get_account(self, account_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/accounts/{account_id}", model=Account)

    def list_accounts(self):
        return self._request_handler.request(request_type=RequestType.GET, uri="/accounts")

    def get_direct_deposit_allocations(self, account_id: str):
        return self._request_handler.request(request_type=RequestType.GET,
                                             uri=f"/accounts/{account_id}/direct_deposit_allocations")

    def get_platform(self, platform_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/platforms/{platform_id}")

    def search_employers_and_platforms(self, search_query: str = None, response_type: ResponseTypes = None,
                                       supported_job: JobTypes = None):
        kwargs = utils.replace_enums(search_query=search_query, response_types=response_type,
                                     supported_jobs=supported_job)
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/search", params=kwargs)

    def list_employers(self, last_updated_timestamp: str = None):
        return self._request_handler.request(request_type=RequestType.GET,
                                             uri="/employers",
                                             params={'last_updated': last_updated_timestamp})

    def list_platforms(self, last_updated_timestamp: str = None, include_esps: bool = False):
        return self._request_handler.request(request_type=RequestType.GET,
                                             uri="/employers",
                                             params={'last_updated': last_updated_timestamp,
                                                     'include_esps': include_esps})

    def get_employer(self, employer_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/employers/{employer_id}")

    def list_paystubs(self, account_id: str, from_date: str = None, to_date: str = None, limit: int = 100):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/accounts/{account_id}/paystubs",
                                             params={
                                                 'from_pay_date': from_date,
                                                 'to_pay_date': to_date,
                                                 'limit': limit
                                             })

    def get_employment(self, account_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/accounts/{account_id}/employment")

    def get_income(self, account_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/accounts/{account_id}/income")

    def get_identity(self, account_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/accounts/{account_id}/identity")

    def list_shifts(self, account_id: str, from_start_date: str = None, to_start_date: str = None,
                    from_end_date: str = None, to_end_date: str = None, limit: int = 100):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/accounts/{account_id}/employment",
                                             params={
                                                 'from_start_date': from_start_date,
                                                 'to_start_date': to_start_date,
                                                 'from_end_date': from_end_date,
                                                 'to_end_date': to_end_date,
                                                 'limit': limit
                                             })

    def get_paystub(self, account_id: str, paystub_id: str):
        return self._request_handler.request(request_type=RequestType.GET,
                                             uri=f"/accounts/{account_id}/paystubs/{paystub_id}")

    def list_completed_jobs(self, account_id: str = None, from_timestamp: str = None, to_timestamp: str = None,
                            job_type: JobTypes = None, link_token_id: str = None, limit: int = 100):
        kwargs = utils.replace_enums(account_id=account_id, from_timestamp=from_timestamp, to_timestamp=to_timestamp,
                                     job_type=job_type, link_token_id=link_token_id, limit=limit)
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/jobs", params=kwargs)

    def create_link_token(self,
                          organization_name: str,
                          job: str,
                          account_type: str,
                          routing_number: str,
                          account_number: str,
                          amount: Union[float, int],
                          employer_id: str,
                          account_name: str,
                          platform_id: str,
                          required_jobs: List[str],
                          skip_intro_scene: bool = False,
                          disable_direct_deposit_splitting: bool = False
                          ):
        return self._request_handler.request(request_type=RequestType.POST, uri="/link_tokens",
                                             data={
                                                 'org_name': organization_name,
                                                 'job': job,
                                                 'account_type': account_type,
                                                 'routing_number': routing_number,
                                                 'account_number': account_number,
                                                 'amount': amount,
                                                 'employer_id': employer_id,
                                                 'account_name': account_name,
                                                 'platform_id': platform_id,
                                                 'required_jobs': required_jobs,
                                                 'skip_intro_scene': skip_intro_scene,
                                                 'disable_direct_deposit_splitting': disable_direct_deposit_splitting
                                             })

    def create_site(self,
                    organization_name: str,
                    job: str,
                    account_type: str,
                    routing_number: str,
                    account_number: str,
                    amount: Union[float, int],
                    employer_id: str,
                    account_name: str,
                    platform_id: str,
                    required_jobs: List[str],
                    redirect_url: str,
                    ttl_seconds: int = 900,
                    skip_intro_scene: bool = False,
                    disable_direct_deposit_splitting: bool = False
                    ):
        return self._request_handler.request(request_type=RequestType.POST, uri="/sites",
                                             data={
                                                 'org_name': organization_name,
                                                 'job': job,
                                                 'account_type': account_type,
                                                 'routing_number': routing_number,
                                                 'account_number': account_number,
                                                 'amount': amount,
                                                 'employer_id': employer_id,
                                                 'account_name': account_name,
                                                 'platform_id': platform_id,
                                                 'required_jobs': required_jobs,
                                                 'redirect_url': redirect_url,
                                                 'ttl': ttl_seconds,
                                                 'skip_intro_scene': skip_intro_scene,
                                                 'disable_direct_deposit_splitting': disable_direct_deposit_splitting
                                             })

    def create_webhook(self, url: str, status: str, enabled_events: List[str]):
        return self._request_handler.request(request_type=RequestType.POST, uri="/webhooks",
                                             data={
                                                 'url': url,
                                                 'status': status,
                                                 'enabled_events': enabled_events
                                             })

    def delete_webhook(self, webhook_id: str):
        return self._request_handler.request(request_type=RequestType.DELETE, uri=f"/webhooks/{webhook_id}")

    def list_webhooks(self):
        return self._request_handler.request(request_type=RequestType.GET, uri="/webhooks")

    def update_webhook(self, webhook_id: str, url: str, status: str, enabled_events: List[str]):
        return self._request_handler.request(request_type=RequestType.PUT, uri=f"/webhooks/{webhook_id}",
                                             data={
                                                 'url': url,
                                                 'status': status,
                                                 'enabled_events': enabled_events
                                             })

    def get_webhook(self, webhook_id: str):
        return self._request_handler.request(request_type=RequestType.GET, uri=f"/webhooks/{webhook_id}")
