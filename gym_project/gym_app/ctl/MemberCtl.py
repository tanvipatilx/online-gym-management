from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import Member
from ..service.member_service import MemberService
from ..service.trainer_service import TrainerService


class MemberCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['name'] = requestForm['name']
        self.form['age'] = requestForm['age']
        self.form['email'] = requestForm['email']
        self.form['phone'] = requestForm['phone']
        self.form['trainer_id'] = requestForm['trainer_id']
        if self.form['trainer_id'] != '':
            trainer = TrainerService().get(self.form['trainer_id'])
            self.form["trainer_name"] = trainer.name

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.name = self.form['name']
        obj.age = self.form['age']
        obj.email = self.form['email']
        obj.phone = self.form['phone']
        obj.trainer_id = self.form['trainer_id']
        obj.trainer_name = self.form['trainer_name']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['age'] = obj.age
        self.form['email'] = obj.email
        self.form['phone'] = obj.phone
        self.form['trainer_id'] = obj.trainer_id
        self.form['trainer_name'] = obj.trainer_name

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['name']):
            inputError['name'] = "Member Name can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['name']):
                inputError['name'] = "Member considers only letters"
                self.form['error'] = True

        if DataValidator.isNull(self.form['age']):
            inputError['age'] = "Age can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['email'])):
            inputError['email'] = "Email can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['phone'])):
            inputError['phone'] = "Phone can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['trainer_id'])):
            inputError['trainer_id'] = "Trainer can not be null"
            self.form['error'] = True

        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.dynamic_preload = TrainerService().preload()
        self.member_preload = self.get_service().preload()

    def display(self, request, params={}):
        res = render(request, self.get_template(), {"form": self.form, 'trainerList': self.dynamic_preload, 'memberList': self.member_preload})
        return res

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            duplicate = self.get_service().get_model().objects.exclude(id=pk).filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Member Name already exists"
                res = render(request, self.get_template(), {"form": self.form, 'trainerList': self.dynamic_preload, 'memberList': self.member_preload})
            else:
                member = self.form_to_model(Member())
                self.get_service().save(member)
                self.form['id'] = member.id
                self.form['error'] = False
                self.form['message'] = "Member updated successfully"
                self.member_preload = self.get_service().preload()
                res = render(request, self.get_template(), {'form': self.form, 'trainerList': self.dynamic_preload, 'memberList': self.member_preload})
            return res
        else:
            duplicate = self.get_service().get_model().objects.filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Member Name already exists"
                res = render(request, self.get_template(), {'form': self.form, 'trainerList': self.dynamic_preload, 'memberList': self.member_preload})
            else:
                member = self.form_to_model(Member())
                self.get_service().save(member)
                self.form['message'] = False
                self.form['message'] = "Member saved successfully"
                self.member_preload = self.get_service().preload()
                res = render(request, self.get_template(), {'form': self.form, 'trainerList': self.dynamic_preload, 'memberList': self.member_preload})
            return res

    def get_template(self):
        return "Member.html"

    def get_service(self):
        return MemberService()
