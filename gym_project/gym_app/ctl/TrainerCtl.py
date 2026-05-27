from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import Trainer
from ..service.trainer_service import TrainerService


class TrainerCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['name'] = requestForm['name']
        self.form['specialization'] = requestForm['specialization']
        self.form['experience'] = requestForm['experience']
        self.form['contact'] = requestForm['contact']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.name = self.form['name']
        obj.specialization = self.form['specialization']
        obj.experience = self.form['experience']
        obj.contact = self.form['contact']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['specialization'] = obj.specialization
        self.form['experience'] = obj.experience
        self.form['contact'] = obj.contact

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['name']):
            inputError['name'] = "Trainer Name can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['name']):
                inputError['name'] = "Trainer Name considers only letters"
                self.form['error'] = True

        if DataValidator.isNull(self.form['specialization']):
            inputError['specialization'] = "Specialization can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['experience'])):
            inputError['experience'] = "Experience can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['contact'])):
            inputError['contact'] = "Contact can not be null"
            self.form['error'] = True

        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.dynamic_preload = self.get_service().preload()

    def _ctx(self):
        return {"form": self.form, "trainerList": self.dynamic_preload}

    def display(self, request, params={}):
        return render(request, self.get_template(), self._ctx())

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            duplicate = self.get_service().get_model().objects.exclude(id=pk).filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Trainer Name already exists"
            else:
                trainer = self.form_to_model(Trainer())
                self.get_service().save(trainer)
                self.form['id'] = trainer.id
                self.form['error'] = False
                self.form['message'] = "Trainer updated successfully"
                self.dynamic_preload = self.get_service().preload()
        else:
            duplicate = self.get_service().get_model().objects.filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Trainer Name already exists"
            else:
                trainer = self.form_to_model(Trainer())
                self.get_service().save(trainer)
                self.form['error'] = False
                self.form['message'] = "Trainer saved successfully"
                self.dynamic_preload = self.get_service().preload()
        return render(request, self.get_template(), self._ctx())

    def get_template(self):
        return "Trainer.html"

    def get_service(self):
        return TrainerService()