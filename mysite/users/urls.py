from .forms import SignUpForm

def signMeUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return #redirect to login
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    return #redirect back to sign up form