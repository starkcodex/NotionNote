from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'appone/welcome.html'


@login_required(login_url='/admin')
def authorize(request):
    return render(request, 'appone/authorize.html', {})