"""
    Legal Entity Management API

    The Legal Entity Management API enables you to manage legal entities that contain information required for verification.  ## Authentication To connect to the Legal Entity Management API, you must use the basic authentication credentials of your web service user. If you don't have one, contact the [Adyen Support Team](https://www.adyen.help/hc/en-us/requests/new). Use the web service user credentials to authenticate your request, for example:  ``` curl -U \"ws12345@Scope.BalancePlatform_YourBalancePlatform\":\"YourWsPassword\" \\ -H \"Content-Type: application/json\" \\ ... ``` Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).  ## Versioning The Legal Entity Management API supports versioning of its endpoints through a version suffix in the endpoint URL. This suffix has the following format: \"vXX\", where XX is the version number.  For example: ``` https://kyc-test.adyen.com/lem/v2/legalEntities ``` ## Going live When going live, your Adyen contact will provide your API credential for the live environment. You can then use the username and password to send requests to `https://kyc-live.adyen.com/lem/v2`.    # noqa: E501

    The version of the OpenAPI document: 2
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""

from ..base import AdyenServiceBase


class DocumentsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(DocumentsApi, self).__init__(client=client)
        self.service = "legalEntityManagement"

    def delete_document(self, id, idempotency_key=None, **kwargs):
        """
        Delete a document
        """
        endpoint = f"/documents/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_document(self, id, idempotency_key=None, **kwargs):
        """
        Get a document
        """
        endpoint = f"/documents/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_document(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a document
        """
        endpoint = f"/documents/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def upload_document_for_verification_checks(self, request, idempotency_key=None, **kwargs):
        """
        Upload a document for verification checks
        """
        endpoint = f"/documents"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)




