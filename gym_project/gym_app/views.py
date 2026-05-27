from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session

from .ctl.TrainerCtl import TrainerCtl
from .ctl.MemberCtl import MemberCtl
from .ctl.MembershipCtl import MembershipCtl
from .ctl.PaymentCtl import PaymentCtl
from .ctl.ExerciseCtl import ExerciseCtl
from .ctl.WorkoutplanCtl import WorkoutplanCtl
from .ctl.EquipmentCtl import EquipmentCtl


@csrf_exempt
def action(request, page="", operation="", id=0):
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        page = "Login"
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    res = ctlObj.execute(request, {"operation": operation, "id": id})
    return res


def index(request):
    res = render(request, 'Welcome.html')
    return res