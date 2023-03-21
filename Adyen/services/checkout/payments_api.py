from ..base import AdyenServiceBase


class PaymentsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PaymentsApi, self).__init__(client=client)
        self.service = "checkout"

    def card_details(self, request, idempotency_key=None, **kwargs):
        """
        Get the list of brands on the card
        """
        endpoint = f"/cardDetails"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def donations(self, request, idempotency_key=None, **kwargs):
        """
        Start a transaction for donations
        """
        endpoint = f"/donations"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payment_methods(self, request, idempotency_key=None, **kwargs):
        """
        Get a list of available payment methods
        """
        endpoint = f"/paymentMethods"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payments(self, request, idempotency_key=None, **kwargs):
        """
        Start a transaction
        """
        endpoint = f"/payments"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def payments_details(self, request, idempotency_key=None, **kwargs):
        """
        Submit details for a payment
        """
        endpoint = f"/payments/details"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def sessions(self, request, idempotency_key=None, **kwargs):
        """
        Create a payment session
        """
        endpoint = f"/sessions"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

