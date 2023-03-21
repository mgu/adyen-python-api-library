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
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_document(self, id, idempotency_key=None, **kwargs):
        """
        Get a document
        """
        endpoint = f"/documents/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_document(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a document
        """
        endpoint = f"/documents/{id}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def upload_document_for_verification_checks(self, request, idempotency_key=None, **kwargs):
        """
        Upload a document for verification checks
        """
        endpoint = f"/documents"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

