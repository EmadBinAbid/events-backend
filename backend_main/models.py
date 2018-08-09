from django.db import models
from django.utils import timezone
import datetime
from simple_history.models import HistoricalRecords

MAX_NAME_LENGTH = 100
MAX_DESC_LENGTH = 500
MAX_TAG_LENGTH = 50
MAX_CONTACT_LENGTH = 100
UPLOAD_USER_IMAGE = None

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    description = models.CharField(max_length = MAX_DESC_LENGTH)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_attendees = models.IntegerField()
    is_public = models.BooleanField()
    organizer = models.ForeignKey('Org', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    history = HistoricalRecords()

class Tags(models.Model):
    name = models.CharField(max_length = MAX_TAG_LENGTH)

class Event_Tags(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE, , related_name = "event_tag_ids")
    tags_id = models.ForeignKey('Tags',on_delete=models.CASCADE)

class Org(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    description = models.CharField(max_length = MAX_DESC_LENGTH)
    contact = models.EmailField(max_length = MAX_CONTACT_LENGTH)
    verified = models.BooleanField()
    history = HistoricalRecords()

class Event_Org(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    org_id = models.ForeignKey('Org',on_delete=models.CASCADE)

class Location(models.Model):
    building = models.CharField(max_length = MAX_NAME_LENGTH)
    room = models.CharField(max_length = MAX_NAME_LENGTH)
    place_id = models.CharField(max_length = MAX_NAME_LENGTH)

class Users(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    contact = models.EmailField(max_length = MAX_CONTACT_LENGTH)
    date_added = models.DateField(auto_now_add = True)
    url = models.ImageField(upload_to = UPLOAD_USER_IMAGE)

class Attendance(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    num_interested = models.IntegerField()
    num_going = models.IntegerField()
