from django.http import HttpResponse
from django.shortcuts import render


def success(request):
    return HttpResponse("Hello, world. You're at the tracking index.")

from tracking.forms import UploadForm
from django.views.generic.edit import FormView

from .file_parser import file_parser

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(UploadView, self).form_valid(form)

def upload_file(request):
    print(request.FILES)
    if request.FILES.getlist('file1') != []:
        #form = UploadForm(request.POST, request.FILES)
        file_parser(request.FILES['file1'])
        #if form.is_valid():
        #    print("Ajeje")
        #    file_parser(request.FILES['file1'])
        #    return HttpResponseRedirect('/success/url/')
    else:
        form = UploadForm()
    return render(request, 'form.html', {'form': form})
