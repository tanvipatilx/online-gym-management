from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import Membership
from ..service.membership_service import MembershipService
from ..service.member_service import MemberService


class MembershipCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['type'] = requestForm['type']
        self.form['start_date'] = requestForm['start_date']
        self.form['end_date'] = requestForm['end_date']
        self.form['fee'] = requestForm['fee']
        self.form['member_id'] = requestForm['member_id']
        if self.form['member_id'] != '':
            member = MemberService().get(self.form['member_id'])
            self.form["member_name"] = member.name

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.member_id = self.form['member_id']
        obj.member_name = self.form['member_name']
        obj.type = self.form['type']
        obj.start_date = self.form['start_date']
        obj.end_date = self.form['end_date']
        obj.fee = self.form['fee']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['member_id'] = obj.member_id
        self.form['member_name'] = obj.member_name
        self.form['type'] = obj.type
        self.form['start_date'] = obj.start_date
        self.form['end_date'] = obj.end_date
        self.form['fee'] = obj.fee

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['member_name']):
            inputError['member_name'] = "Member name can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['type'])):
            inputError['type'] = "Type can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['start_date'])):
            inputError['start_date'] = "Start date can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['end_date'])):
            inputError['end_date'] = "End date can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['fee'])):
            inputError['fee'] = "Fee can not be null"
            self.form['error'] = True

        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.dynamic_preload = MemberService().preload()
        self.membership_preload = self.get_service().preload()

    def display(self, request, params={}):
        return render(request, self.get_template(), {"form": self.form, 'memberList': self.dynamic_preload, 'membershipList': self.membership_preload})

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            membership = self.form_to_model(Membership())
            self.get_service().save(membership)
            self.form['id'] = membership.id
            self.form['error'] = False
            self.form['message'] = "Membership updated successfully"
            self.membership_preload = self.get_service().preload()
            return render(request, self.get_template(), {"form": self.form, 'memberList': self.dynamic_preload, 'membershipList': self.membership_preload})
        else:
            membership = self.form_to_model(Membership())
            self.get_service().save(membership)
            self.form['error'] = False
            self.form['message'] = "Membership saved successfully"
            self.membership_preload = self.get_service().preload()
            return render(request, self.get_template(), {'form': self.form, 'memberList': self.dynamic_preload, 'membershipList': self.membership_preload})

    def get_template(self):
        return "Membership.html"

    def get_service(self):
        return MembershipService()
