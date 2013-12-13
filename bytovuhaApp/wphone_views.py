# encoding=utf-8

from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def login_action(request, username, password):

	try:
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(str(user.customer.id))
			else:
				return HttpResponse("-1")
		else:
			return HttpResponse("-1")
	except Exception:
		return HttpResponse("-1")