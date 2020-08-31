from django.http import HttpResponse
from django.shortcuts import redirect

# A decorator is a function that takes in another funtion as a 
# parameter and lets us ad some functonality
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:# if user is authenticated take them to the homepage
            return redirect('home')

        else:# If youre logged in then you wont be able to view the login or sign up page
            return view_func(request, *args, **kwargs)

    return wrapper_func