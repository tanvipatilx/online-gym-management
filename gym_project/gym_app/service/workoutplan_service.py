from ..models import WorkoutPlan
from ..utility.DataValidator import DataValidator
from .base_service import base_service
from django.db import connection


class WorkoutplanService(base_service):

    def search(self, params):
        pageNo = (params['pageNo'] - 1) * self.pageSize
        sql = 'select * from gym_worplan where 1=1'
        val = params.get('name', None)
        if (DataValidator.isNotNull(val)):
            sql += " and name like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('name', 'description', 'duration','exercise_id','exercise_name','member_id','member_name')
        res = {
            "data": [],
        }
        params["index"] = ((params['pageNo'] - 1) * self.pageSize)
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            params['maxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get_model(self):
        return WorkoutPlan