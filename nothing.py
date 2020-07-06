def doc_create(request):
    if request.method == 'POST':
        print('Method : POST')
        form = DocumentForm(request.POST)
        if form.is_valid():
            # document = form.save(commit=False)
            form.save()
            return redirect('https://www.naver.com')
        else:
            print('Form is not valid')
            print(form.errors)
            return redirect('https://www.daum.net')
    else:
        print('Method', request.method)
        form = DocumentForm()

        context = {'form': form}
        # return redirect('https://www.naver.com')
        return render(request, 'forms.html', context)

    'InvestorType',