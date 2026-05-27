from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ..utility.DataValidator import DataValidator
from ..models import WorkoutPlan
from ..service.workoutplan_service import WorkoutplanService
from ..service.member_service import MemberService
from ..service.exercise_service import ExerciseService


class WorkoutplanCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['name'] = requestForm['name']
        self.form['description'] = requestForm['description']
        self.form['duration'] = requestForm['duration']
        self.form['exercise_id'] = requestForm['exercise_id']
        if self.form['exercise_id']:
            exercise = ExerciseService().get(self.form['exercise_id'])
            self.form['exercise_name'] = exercise.name if exercise else ''
        else:
            self.form['exercise_name'] = ''
        self.form['member_id'] = requestForm['member_id']
        if self.form['member_id']:
            member = MemberService().get(self.form['member_id'])
            self.form['member_name'] = member.name if member else ''
        else:
            self.form['member_name'] = ''

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if pk > 0:
            obj.id = pk
        obj.name = self.form['name']
        obj.description = self.form['description']
        obj.duration = self.form['duration']
        obj.exercise_id = self.form['exercise_id']
        obj.exercise_name = self.form['exercise_name']
        obj.member_id = self.form['member_id']
        obj.member_name = self.form['member_name']
        return obj

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['description'] = obj.description
        self.form['duration'] = obj.duration
        self.form['exercise_id'] = obj.exercise_id
        self.form['exercise_name'] = obj.exercise_name
        self.form['member_id'] = obj.member_id
        self.form['member_name'] = obj.member_name

        # Validate Form

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']

        if DataValidator.isNull(self.form['name']):
            inputError['name'] = "Workoutplan Name can not be null"
            self.form['error'] = True

        else:
            if DataValidator.isalphacehck(self.form['name']):
                inputError['name'] = "Workoutplan Name considers only letters"
                self.form['error'] = True

        if DataValidator.isNull(self.form['description']):
            inputError['description'] = "Description can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['duration'])):
            inputError['duration'] = "Duration can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['exercise_id'])):
            inputError['exercise_id'] = "Exercise id can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['exercise_name'])):
            inputError['exercise_name'] = "Exercise name can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['member_id'])):
            inputError['member_id'] = "Member id can not be null"
            self.form['error'] = True

        if (DataValidator.isNull(self.form['member_name'])):
            inputError['member_name'] = "Member name can not be null"
            self.form['error'] = True

        return self.form['error']

    def preload(self, request, params={}):
        super().preload(request, params)
        self.member_preload = MemberService().preload()
        self.exercise_preload = ExerciseService().preload()
        self.workoutplan_preload = self.get_service().preload()

    def _ctx(self):
        return {"form": self.form, "memberList": self.member_preload, "exerciseList": self.exercise_preload, "workoutplanList": self.workoutplan_preload}

    def display(self, request, params={}):
        return render(request, self.get_template(), self._ctx())

    def submit(self, request, params={}):
        if (params['id'] > 0):
            pk = params['id']
            duplicate = self.get_service().get_model().objects.exclude(id=pk).filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Workoutplan Name already exists"
            else:
                workoutplan = self.form_to_model(WorkoutPlan())
                self.get_service().save(workoutplan)
                self.form['id'] = workoutplan.id
                self.form['error'] = False
                self.form['message'] = "Workoutplan updated successfully"
                self.workoutplan_preload = self.get_service().preload()
        else:
            duplicate = self.get_service().get_model().objects.filter(name=self.form['name'])
            if duplicate.count() > 0:
                self.form['error'] = True
                self.form['message'] = "Workoutplan Name already exists"
            else:
                workoutplan = self.form_to_model(WorkoutPlan())
                self.get_service().save(workoutplan)
                self.form['error'] = False
                self.form['message'] = "Workoutplan saved successfully"
                self.workoutplan_preload = self.get_service().preload()
        return render(request, self.get_template(), self._ctx())

    def get_template(self):
        return "Workoutplan.html"

    def get_service(self):
        return WorkoutplanService()