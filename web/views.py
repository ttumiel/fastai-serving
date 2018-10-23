from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UploadFileForm
from .utils import evaluate

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            evaluate(request.FILES['image'])
            # print(request.FILES['image'])
            return HttpResponseRedirect('/results', )
    form = UploadFileForm()
    return render(request, 'web/index.html', {'form': form})

def results(request):
    return render(request, 'web/results.html')#, {'result': result})