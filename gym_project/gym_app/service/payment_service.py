from ..models import Payment
from .base_service import base_service


class PaymentService(base_service):

    def get_model(self):
        return Payment