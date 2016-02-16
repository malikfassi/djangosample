from django.contrib.auth import authenticate, login, logout
from authentication.forms import ConnexionForm, RegistrationForm
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail
from authentication.models import UserProfile
from datetime import datetime

from django.conf import settings
from django.shortcuts import redirect


def redirect_if_logged(redirect_url):
    def decorator(a_view):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated():
                return redirect(redirect_url)
            return a_view(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@ensure_csrf_cookie
@redirect_if_logged("/applist")
def login_user(request):
    if request.user.is_authenticated():
        return redirect("/")
    error = False
    if request.method == "POST":
        if "SendEmail" in request.POST:
            allusers = UserProfile.objects.all()
            for eachuser in allusers:
                if (eachuser.subscribed):
                    send_mail('My django-app', 'Hello, ' + eachuser.username +".\n It is : "+ datetime.now().strftime("%I:%M%p on %B %d, %Y"), 'malikfassifihri@gmail.com',[eachuser.email], fail_silently=False)
        else:
            form = ConnexionForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return  redirect("/applist")
                else:
                    error = True
    else:
        form = ConnexionForm()
    return render(request, 'login.html', locals())

@ensure_csrf_cookie
@login_required                                                                                           
def logout_user(request):
    logout(request)                                                                         
    return redirect(reverse(login_user))

@ensure_csrf_cookie
def signin(request):
    args = {}
    args.update(csrf(request))
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()
            return (HttpResponseRedirect("/applist"))
    else:
        args['form'] = RegistrationForm()
    return (render_to_response('signin.html', args, context_instance=RequestContext(request)))