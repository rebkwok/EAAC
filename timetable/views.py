from django.shortcuts import render, HttpResponse, get_object_or_404


def timetable(request):

    return render(request, 'timetable/timetable.html', {'section': 'timetable'})