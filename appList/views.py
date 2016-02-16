from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf
from .forms import *
from django.shortcuts import render, redirect, render_to_response
from .models import Application
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
	if request.user.is_staff:
		applications = Application.objects.all()
	else:
		applications = Application.objects.filter(access="PU")
	not_empty = len(applications)
	context = RequestContext(request, {
		'not_empty' : not_empty,
		'applications' : applications,
		})
	return render(request, 'index.html', context)

@login_required
@ensure_csrf_cookie
def edit(request, appId):
	args = {}
	args.update(csrf(request))
	app = get_object_or_404(Application, id=appId)
	if (request.method == 'POST'):
		if 'delete' in request.POST:
			app.delete()
			return (redirect("/applist"))
		form = UploadForm(request.POST, request.FILES, instance=app)
		args['form'] = form
		if form.is_valid():
			form.save()
			return (redirect("/applist"))
	else:
		form = UploadForm(instance=app)
		context = RequestContext(request, {
			'form' : form,
		})
	return (render_to_response('edit.html', args, context))

@login_required
@ensure_csrf_cookie
def upload(request):
	args = {}
	args.update(csrf(request))
	if (request.method == 'POST'):
		form = UploadForm(request.POST, request.FILES)
		print request.FILES	
		args['form'] = form
		if form.is_valid():
			form.save()
			return (redirect("/"))
	else:
		args['form'] = UploadForm()
	return (render_to_response('upload.html', args, context_instance=RequestContext(request)))