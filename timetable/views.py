from django.shortcuts import render, HttpResponse, get_object_or_404
from timetable.models import Session
from django_tables2   import RequestConfig
from timetable.tables  import SessionTable

def timetable(request):
    table = SessionTable(Session.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'timetable/timetable.html', {'section': 'timetable', 
                                                        'table': table})