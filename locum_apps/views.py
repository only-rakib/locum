from django.shortcuts import render

# Create your views here.


def apply_view(request):
    return render(request, 'locum_apply.html')


def contact_us_view(request):
    return render(request, 'locum_contact_us.html')


def job_search_view(request):
    return render(request, 'locum_job_search.html')


def resourse_view(request):
    return render(request, 'locum_resourse.html')
