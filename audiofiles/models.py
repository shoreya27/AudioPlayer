from django.db import models
import json
# Create your models here.
#first Model #songtype file
class SongFile(models.Model):
    '''
    This class will represent all song type file in db
    All fields are necessary
    '''
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}.{self.pk}"

    def get_model_as_json(self):

        d = dict()
        d["song_id"] = self.pk
        d["name"] = self.name
        d["durations"] = str(self.duration)+" secs"
        d["uploaded_time"] = self.uploaded_time
        
        return d

class PodcastFile(models.Model):
    '''
    This class will represent all podcast 
    '''
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = models.TextField()

    def __str__(self):
        return f"{self.name}.{self.pk}"

    def get_model_as_json(self):
        d = dict()
        d["podcast_id"] = self.pk
        d["name"] = self.name
        d["durations"] = str(self.duration)+" secs"
        d["uploaded_time"] = self.uploaded_time
        d["host"] = self.host
        d["participants"] = json.loads(self.participants)
        return d

class AudiobookFile(models.Model):
    '''
    Class will represent all Audiobook objects
    '''
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    narrator = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}.{self.pk}"

    def get_model_as_json(self):
        d = dict()
        d["audiobook_id"] = self.pk
        d["title"] = self.name
        d["durations"] = str(self.duration)+" secs"
        d["uploaded_time"] = self.uploaded_time
        d["narrator"] = self.narrator
        d["author"] = self.author
        return d