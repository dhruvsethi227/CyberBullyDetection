from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TranForm
from profanity import profanity
from base import algo

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def input_view(request):
    color = "#0099ff"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TranForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            text = form.cleaned_data['text']
            l1 = algo.get_final(text)
            context = {}
            context['value'] = l1[0]
            context['magnitude'] = l1[1]
            if l1[0] < 0:
                return render(request, 'bad.html', context)
            else:
                return render(request, 'good.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TranForm()

    return render(request, 'home.html', {'form': form})

