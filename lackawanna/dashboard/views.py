from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def IndexView(request):
    return render(request=request,
                  template_name='dashboard/base.html')
