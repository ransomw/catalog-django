from pdb import set_trace as st

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.template import RequestContext

from .forms import LoginForm

TEMPLATE_DIR = 'cauth'

def login(request):
    def render_form(form):
        # RequestContext handles csrf token regeneration
        return render(request, TEMPLATE_DIR + '/login.html',
                      RequestContext(request,
                                     {'form': form}))

    if request.method == 'GET':
        form = LoginForm()
        return render_form(form)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render_form(form)
        elif form.is_sign_in():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # todo: custom user model
            return render_form(form)
        elif form.is_sign_up():
            print("got sign up request")
            return render_form(form)
        else:
            return HttpResponseBadRequest(
                "must specify sign-up or sign-in")
