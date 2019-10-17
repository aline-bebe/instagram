from django.shortcuts import render
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to instagram')

def insta(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('insta')
    else:
        form = NewsLetterForm()
    return render(request, 'all-insta/insta.html', {"letterForm":form})
