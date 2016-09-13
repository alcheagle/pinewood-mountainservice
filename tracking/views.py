from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the tracking index.")

from tracking.forms import UploadForm
from django.views.generic.edit import FormView

from file_parser import file_parser

class UploadView(FormView):
    template_name = 'tracking/form.html'
    form_class = UploadForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(UploadView, self).form_valid(form)

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_parser(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})