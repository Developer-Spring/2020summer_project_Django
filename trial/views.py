from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
from .forms import DocumentForm

# Create your views here.
def index(request):
    document = Document.objects
    context = {'document': document}
    return render(request, 'forms.html', context)

def doc_create(request):
    if request.method == 'POST':
        # print('Method : POST')
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            return redirect(request, 'trial/Result_page.html')
        else:
            # print('Form is not valid')
            # print(form.errors)
            return redirect('https://www.daum.net')
    else:
        print('Method', request.method)
        form = DocumentForm()

        context = {'form': form}
        # return redirect('https://www.naver.com')
        return render(request, 'forms.html', context)

def doc_result(request, document_id):
    document = Document.objects.get(id=document_id)
    context = {'document': document}
    return render(request, 'forms.html', context)


    # if request.method == "POST":
    #     form = ResultForm(request.POST)
    #     if form.is_valid():
    #         result = form.save(commit=False)
    #         result.save()
    #         return redirect('trial:index')
    # else:
    #     form = ResultForm()
    # context = {'document': document, 'form': form}
    # return render(request, 'trial/forms.html', context)
