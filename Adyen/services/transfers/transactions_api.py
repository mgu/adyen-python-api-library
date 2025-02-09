from ..base import AdyenServiceBase


class TransactionsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TransactionsApi, self).__init__(client=client)
        self.service = "transfers"

    def get_all_transactions(self, idempotency_key=None, **kwargs):
        """
        Get all transactions
        """
        endpoint = f"/transactions"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_transaction(self, id, idempotency_key=None, **kwargs):
        """
        Get a transaction
        """
        endpoint = f"/transactions/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

