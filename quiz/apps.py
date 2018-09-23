# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.apps import AppConfig,apps

class QuizConfig(AppConfig):
    name = 'quiz'
  
    def ready(self):
    	from actstream import registry
    	registry.register(self.get_model('Feed'))
    
