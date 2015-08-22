from pdb import set_trace as st

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.core.urlresolvers import reverse

from .forms import LoginForm

TEMPLATE_DIR = 'cauth'

User = get_user_model()

def login(request):
    def render_form(form):
        # RequestContext handles csrf token regeneration
        return render(request, TEMPLATE_DIR + '/login.html',
                      RequestContext(request,
                                     {'form': form}))

    # todo: control-flow --- not obvious that this function
    #       alwayws returns not None
    if request.method == 'GET':
        form = LoginForm()
        return render_form(form)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render_form(form)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        if form.is_sign_in():
            user = authenticate(username=email, password=password)
            if user is None:
                form.add_error(
                    None,
                    ("incorrect username or password"))
                return render_form(form)
            else:
                _login(request, user)
                return HttpResponseRedirect(reverse('home'))
        elif form.is_sign_up():
            name = form.cleaned_data['name']
            user = User.objects.create_user(
                email=email, password=password)
            # todo: error-handling of, e.g., duplicate usernames
            #       and misc. unspecified server errors, e.g., db error
            #       ... cf. stock views
            user.name = name
            user.save()
            _login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseBadRequest(
                "must specify sign-up or sign-in")

def logout(request):
    _logout(request)
    return HttpResponseRedirect(reverse('home'))
