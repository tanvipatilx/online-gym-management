from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import Payment
from ..service.payment_service import PaymentService
from ..service.member_service import MemberService


class PaymentCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['member_id'] = requestForm['member_id']
        if self.form['member_id']:
            member = MemberService().get(self.form['member_id'])
            self.form['member_name'] = member.name if member else ''
        else:
            self.form['member_name'] = ''
        self.form['amount'] = requestForm['amount']
        self.form['payment_date'] = requestForm['payment_date']
        self.form['method'] = requestForm['method']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.member_id = self.form['member_id']
        obj.member_name = self.form['member_name']
        obj.amount = self.form['amount']
        obj.payment_date = self.form['payment_date']
        obj.method = self.form['method']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['member_id'] = obj.member_id
        self.form['member_name'] = obj.member_name
        self.form['amount'] = obj.amount
        self.form['payment_date'] = obj.payment_date
        self.form['method'] = obj.method

        # Validate Form

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['member_id']):
            inputError['member_id'] = "Membership ID can not be null"
            self.form['error'] = True

        else:
            if not DataValidator.isalphacehck(self.form['member_id']):
                inputError['member_id'] = "Membership ID must be a number"
                self.form['error'] = True
            elif not MemberService().get(self.form['member_id']):
                inputError['member_id'] = "Member not found"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['amount'])):
            inputError['amount'] = "Amount can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['payment_date'])):
            inputError['payment_date'] = "Payment date can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['method'])):
            inputError['method'] = "Method can not be null"
            self.form['error'] = True

        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.dynamic_preload = MemberService().preload()
        self.payment_preload = self.get_service().preload()

    def display(self, request, params={}):
        return render(request, self.get_template(), {"form": self.form, "memberList": self.dynamic_preload, "paymentList": self.payment_preload})

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            payment = self.form_to_model(Payment())
            self.get_service().save(payment)
            self.form['id'] = payment.id
            self.form['error'] = False
            self.form['message'] = "Payment updated successfully"
        else:
            payment = self.form_to_model(Payment())
            self.get_service().save(payment)
            self.form['error'] = False
            self.form['message'] = "Payment saved successfully"
        self.payment_preload = self.get_service().preload()
        return render(request, self.get_template(), {"form": self.form, "memberList": self.dynamic_preload, "paymentList": self.payment_preload})

    def get_template(self):
        return "Payment.html"

    def get_service(self):
        return PaymentService()