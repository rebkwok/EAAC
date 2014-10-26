from django.shortcuts import render, get_object_or_404
from instructors.models import Instructor

def instructors(request):
    instructor_list = Instructor.objects.all().order_by('name')
    return render(request, 'instructors/instructors.html', {'section': 'instructors',
                                                        'instructors': instructor_list,})
def instructor_info(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    return render(request, 'instructors/instructors.html', {'section': 'instructors', 'instructor': instructor,
                                                        })
