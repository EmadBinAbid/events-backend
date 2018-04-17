from django.db import models
from django.utils import timezone
import datetime
import reversion

MAX_NAME_LENGTH = 100
MAX_DESC_LENGTH = 500
MAX_TAG_LENGTH = 50
MAX_CONTACT_LENGTH = 100
UPLOAD_USER_IMAGE = None

# Create your models here.
@reversion.register()
class Event(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    description = models.CharField(max_length = MAX_DESC_LENGTH)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    num_attendees = models.IntegerField()
    is_public = models.BooleanField()
    organizer = models.ForeignKey('Org', on_delete=CASCADE)

class Tags(models.Model):
    name = models.CharField(max_length = MAX_TAG_LENGTH)

class Event_Tags(models.Model):
    event_id = models.ForeignKey('Event', on_delete=CASCADE)
    tags_id = models.ForeignKey('Tags',on_delete=CASCADE)

class Org(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    description = models.CharField(max_length = MAX_DESC_LENGTH)
    contact = models.EmailField(max_length = MAX_CONTACT_LENGTH)
    verified = models.BooleanField()

class Event_Org(models.Model):
    event_id = models.ForeignKey('Event', on_delete=CASCADE)
    org_id = models.ForeignKey('Org',on_delete=CASCADE)

class Location(models.Model):
    building = models.CharField(max_length = MAX_NAME_LENGTH)
    room = models.CharField(max_length = MAX_NAME_LENGTH)
    place_id = models.CharField(max_length = MAX_NAME_LENGTH)

class Users(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    contact = models.EmailField(max_length = MAX_CONTACT_LENGTH)
    data_added = models.DateField(auto_now_add = True)
    url = models.ImageField(upload_to = UPLOAD_USER_IMAGE)
