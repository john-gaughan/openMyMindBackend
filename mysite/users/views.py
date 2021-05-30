from .forms import SignUpForm, LoginForm
# from .models import User
from django.http import JsonResponse, HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json

def signMeUp(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
    # print(request.method)
        if data['password'] == data['confirm_pass']:
            # form = SignUpForm(request.POST)
            # process the data in form.cleaned_data as required
            # u = User(data['first_name'],data['last_name'],data['username'],data['email'],data['password']) #this for models.User that I made.. unnecsary cuz built in User model
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            # ...
            # redirect to a new URL:
            print("hi")
            # print(u.to_dict())
            return JsonResponse(data)
        # return JsonResponse({"test":3})
        # if a GET (or any other method) we'll create a blank form
        else:
            pass
    print("should not get here")
    return HttpResponse("You are at the sign up page.")

def logMeIn(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return None
    # if a GET (or any other method) we'll create a blank form
    return HttpResponse("You are at the login page.")