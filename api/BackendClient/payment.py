import mercadopago
from django.conf import settings

# url = "https://7276-181-176-72-46.ngrok-free.app/api/v1/webhook/"
url_notification = "http://localhost:5173/pricing"
if not settings.DEBUG:
    # url = "https://nginxpm.lexcom.tech/api/v1/webhook"
    url_notification = "https://lexcom.tech/pricing"


class PaymentApiClient():

    def __init__(self, access_token, data):
        self.access_token = access_token
        self.data = data

    def get_mercadopago_client(self):
        sdk = mercadopago.SDK(self.access_token)
        return sdk

    def create_preference(self):
        client = self.get_mercadopago_client()
        item = {
            "title": self.data.get('title'),
            "quantity": 1,
            "unit_price": float(self.data.get('price')),
            "currency_id": "USD"
        }

        preference_data = {
            "items": [item],
            "back_urls": {
                "success": url_notification,
                "failure": url_notification,
                "pending": url_notification
            },
            "auto_return": "approved",
            # "notification_url": url
        }

        preference_response = client.preference().create(preference_data)
        preference = preference_response["response"]
        return preference


class NotificationApiClient():

    def __init__(self, access_token):
        self.access_token = access_token

    def get_notification_client(self):
        sdk = mercadopago.SDK(self.access_token)
        return sdk

    def get_payment_notification(self, id_):
        client = self.get_notification_client()
        request = client.payment().get(id_)
        return request
