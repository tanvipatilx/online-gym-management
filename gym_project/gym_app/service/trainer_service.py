from ..models import Trainer
from ..utility.DataValidator import DataValidator
from .base_service import base_service
from django.db import connection


class TrainerService(base_service):

    def search(self, params):
        pageNo = (params['pageNo'] - 1) * self.pageSize
        sql = 'select * from gym_trainer where 1=1'
        val = params.get('name', None)
        if (DataValidator.isNotNull(val)):
            sql += " and name like '" + val + "%%'"
        sql += " limit %s, %s"
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('name', 'specialization', 'experience','contact')
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
        return Trainer