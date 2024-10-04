from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .forms import SearchForm
from .utils import generate_instagram_profile_search_url


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_terms = form.cleaned_data['searchTerms']
            profile_type = form.cleaned_data['profileType']
            include_terms = form.cleaned_data.get('includeTerms', '')
            exclude_terms = form.cleaned_data.get('excludeTerms', '')
            url = generate_instagram_profile_search_url(search_terms=search_terms,profile_type=profile_type,include_terms=include_terms,exclude_terms=exclude_terms)
            
            return JsonResponse({'url': url})

    else:
        form = SearchForm()
    
    return render(request,"index.html",{'form': form})



def contact(request):
    if request.method == 'POST':
       
        return JsonResponse({'status': 'success'})

    return render(request,"contact.html")