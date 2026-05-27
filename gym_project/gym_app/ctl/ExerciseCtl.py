from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import Exercise
from ..service.exercise_service import ExerciseService


class ExerciseCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['name'] = requestForm['name']
        self.form['muscle_group'] = requestForm['muscle_group']
        self.form['reps'] = requestForm['reps']
        self.form['sets'] = requestForm['sets']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.name = self.form['name']
        obj.muscle_group = self.form['muscle_group']
        obj.reps = self.form['reps']
        obj.sets = self.form['sets']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['muscle_group'] = obj.muscle_group
        self.form['reps'] = obj.reps
        self.form['sets'] = obj.sets

    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['name']):
            inputError['name'] = "Exercise Name can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['name']):
                inputError['name'] = "Exercise Name considers only letters"
                self.form['error'] = True

        if DataValidator.isNull(self.form['muscle_group']):
            inputError['muscle_group'] = "Muscle group can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['reps'])):
            inputError['reps'] = "Reps can not be null"
            self.form['error'] = True


        if (DataValidator.isNull(self.form['sets'])):
            inputError['sets'] = "Sets can not be null"
            self.form['error'] = True

        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.dynamic_preload = self.get_service().preload()

    def _ctx(self):
        return {"form": self.form, "exerciseList": self.dynamic_preload}

    def display(self, request, params={}):
        return render(request, self.get_template(), self._ctx())

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            duplicate = self.get_service().get_model().objects.exclude(id=pk).filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Exercise Name already exists"
            else:
                exercise = self.form_to_model(Exercise())
                self.get_service().save(exercise)
                self.form['id'] = exercise.id
                self.form['error'] = False
                self.form['message'] = "Exercise updated successfully"
                self.dynamic_preload = self.get_service().preload()
        else:
            duplicate = self.get_service().get_model().objects.filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Exercise Name already exists"
            else:
                exercise = self.form_to_model(Exercise())
                self.get_service().save(exercise)
                self.form['error'] = False
                self.form['message'] = "Exercise saved successfully"
                self.dynamic_preload = self.get_service().preload()
        return render(request, self.get_template(), self._ctx())

    def get_template(self):
        return "Exercise.html"

    def get_service(self):
        return ExerciseService()