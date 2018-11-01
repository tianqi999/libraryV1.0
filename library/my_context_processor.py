#coding=utf-8

from .models import *
import jsonpickle

def mainfunc(request):
    user = request.session.get('user','')

    if user:
        user = jsonpickle.loads(user)

    return {"info":user}