from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
	topics = content.objects.all()
	return render(request,'main.html',{'topics':topics})