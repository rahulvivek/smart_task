# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'login.html'
