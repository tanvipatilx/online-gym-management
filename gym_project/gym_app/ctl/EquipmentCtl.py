from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render

from ..service.equipment_service import EquipementService
from ..utility.DataValidator import DataValidator
from ..models import Equipment
from ..service.equipment_service import EquipementService


class EquipmentCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['name'] = requestForm['name']
        self.form['type'] = requestForm['type']
        self.form['maintenance_date'] = requestForm['maintenance_date']
        self.form['status'] = requestForm['status']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.name = self.form['name']
        obj.type = self.form['type']
        obj.maintenance_date = self.form['maintenance_date']
        obj.status = self.form['status']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['type'] = obj.type
        self.form['maintenance_date'] = obj.maintenance_date
        self.form['status'] = obj.status

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['name']):
            inputError['name'] = "Equipment Name can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['name']):
                inputError['name'] = "Equipment Name considers only letters"
                self.form['error'] = True

        if DataValidator.isNull(self.form['type']):
            inputError['type'] = "Type can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['maintenance_date'])):
            inputError['maintenance_date'] = "Maintenance date can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['status'])):
            inputError['status'] = "Status can not be null"
            self.form['error'] = True


        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.dynamic_preload = self.get_service().preload()

    def _ctx(self):
        return {"form": self.form, "equipmentList": self.dynamic_preload}

    def display(self, request, params={}):
        return render(request, self.get_template(), self._ctx())

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            duplicate = self.get_service().get_model().objects.exclude(id=pk).filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Equipment Name already exists"
            else:
                equipment = self.form_to_model(Equipment())
                self.get_service().save(equipment)
                self.form['id'] = equipment.id
                self.form['error'] = False
                self.form['message'] = "Equipment updated successfully"
                self.dynamic_preload = self.get_service().preload()
        else:
            duplicate = self.get_service().get_model().objects.filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Equipment Name already exists"
            else:
                equipment = self.form_to_model(Equipment())
                self.get_service().save(equipment)
                self.form['error'] = False
                self.form['message'] = "Equipment saved successfully"
                self.dynamic_preload = self.get_service().preload()
        return render(request, self.get_template(), self._ctx())

    def get_template(self):
        return "Equipment.html"

    def get_service(self):
        return EquipementService()