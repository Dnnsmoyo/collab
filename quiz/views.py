# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Profile, Feed
#from .forms import FeedForm
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_registration.forms import RegistrationForm
from actstream import action
from actstream.models import Action
from django.contrib.auth.models import User
from actstream.actions import follow, unfollow
import json

from django.contrib import auth
from django.http import HttpResponse
from django.views import View

# Create your views here.
def front_page(request):
	return render(request,'landing_page.html')

def register(request):
	form = RegistrationForm()
	return render(request,'django_registration/registration_form.html')

def reset(request):
	return render(request,'registration/password_reset_form.html')

def index_view(request):
	act_count = Action.objects.count()
	act = Action.objects.all().order_by('-timestamp')
	feed = Feed.objects.all().order_by('-time')
	pros = Profile.objects.all()
	profile = Profile.objects.filter(user=request.user)
	#question = Question.objects.all()
	return render(request,'quiz.html',{'act':act,'feed':feed,'profile':profile,'pros':pros,'act_count':act_count})

class ProfileDetail(DetailView):
	model = Profile

	def get_context_data(self, **kwargs):
		context = super(ProfileDetail,self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

def follow_me(request):
	follow(request.user, User)
	print("now following")

class FeedFormView(CreateView):
	template_name = 'quiz/feed_form.html'
	model = Feed
	fields = ['text']
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		action.send(self.request.user, verb='posted new content')
		return super(FeedFormView, self).form_valid(form)

class ProfileFormView(CreateView):
	template_name = 'quiz/profile_form.html'
	model = Profile
	fields = ['profession','image','bio']
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ProfileFormView, self).form_valid(form)

class BookmarkView(View):
    # This variable will set the bookmark model to be processed
    model = None

    def post(self, request, pk):
        # We need a user
        user = auth.get_user(request)
        # Trying to get a bookmark from the table, or create a new one
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # If no new bookmark has been created,
        # Then we believe that the request was to delete the bookmark
        if not created:
            bookmark.delete()

        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type="application/json"
        )