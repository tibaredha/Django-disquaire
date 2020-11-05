from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tiba(request):
    return HttpResponse("Hello, world. You're at the polls tiba.")

def redha(request):
    nom = "redha"
    return HttpResponse("""
	<!DOCTYPE html>
	<html>
		<head>
		</head>
			<body>
				<h1>Hello, world. You're at the polls."""+nom+"""<h1>
			</body>
	</html>
	""")
def mimi(request):
	return render(request,"index.html",{'Nom':'redha','date':datetime.now})