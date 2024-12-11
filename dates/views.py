from django.shortcuts import render
from .services import get_sheet_upcoming_dates
from .services import get_sheet_past_results

# Create your views here.

def get_dates(request):
    return render(request, 'dates.html')

def get_results(request):
    return render(request, 'results.html')

def get_info(request):
    return render(request, 'info.html')

def get_index(request):
    return render(request, 'index.html')

def get_base(request):
    return render(request, 'base.html')

def upcoming_dates(request):
    api_id = 'fvi6b7rkv2z2b'
    tab_name = 'upcoming_quizzes'
    sheet_data = get_sheet_upcoming_dates(api_id)

    return render(request, 'dates.html', {'sheet_data': sheet_data})

def past_results(request):
    api_id = 'fvi6b7rkv2z2b'
    tab_name = 'past_quizzes_normal'
    sheet_data = get_sheet_past_results(api_id)

    return render(request, 'results.html', {'sheet_data': sheet_data})