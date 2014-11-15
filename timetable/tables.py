import django_tables2 as tables
from timetable.models import Session

class SessionTable(tables.Table):
    
    class Meta:
        model = Session
        # add class="paleblue" to <table> tag
        order_by = ("session_date", "start_time")
        attrs = {"class": "paleblue"}
        fields = ("session_type", "discipline", "level", "instructor", "session_date", 
                    "start_time", "end_time", "location", "spaces" )
        sequence = ("session_type", "discipline", "level", "instructor", "session_date", 
                    "start_time", "end_time", "location", "spaces" )
                    