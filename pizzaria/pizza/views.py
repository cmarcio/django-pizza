from django.http import HttpResponse
from django.shortcuts import render

def menu(Request):
	return HttpResponse("Hello Word")