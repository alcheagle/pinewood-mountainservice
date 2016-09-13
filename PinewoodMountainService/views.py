from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

from PinewoodMountainService.forms import MainForm
from django.views.generic.edit import FormView

class MainPageView(FormView):
    template_name = 'main/form.html'
    form_class = MainForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(MainPageView, self).form_valid(form)

def upload_file(request):
    if request.method == 'POST':
        form = MainForm(request.POST, request.FILES)
        if form.is_valid():
            file_parser(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = MainForm()
    return render(request, 'upload.html', {'form': form})