import json
from django.http import JsonResponse
from django.views import View
from .models import *
from django.views.decorators.http import require_http_methods

'''
Implement create, read, upload, and delete endpoints for an audio file as defined below:
'''

class FileTypeException(Exception):
    pass


def check_participant_strngth(word):
    if len(word) > 100:
        raise ValueError("participant value exceed 100")

@require_http_methods(["POST"])
def create_audio_file(request):
    '''
    Single Api to create AudioFile object in db
    Audiofile can be of any of 3 types
    >song
    >audiobook
    >podcast
    '''
    result = dict()
    try:
        data = json.loads(request.body)
        #Note : {"song":"s", "podcast":"p", "audiobook":"ab"}

        file_type = data.get("file_type", None)
        if not file_type:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")
    
        #take metadata now
        #common parameters first
        name = data["name"]
        duration = data["duration"]

        if file_type == "s":
            #create a song file object
            obj = SongFile.objects.create(name=name,duration=duration)
        
        elif file_type == "p":
            #create a podcast file object
            host = data["host"]
            participants = data.get("participants",[])#optional
            if len(participants) > 10:
                raise ValueError("participants cant be more than 10")
            for word in participants:
                check_participant_strngth(word)
            
            obj = PodcastFile.objects.create(name = name, duration = duration, host = host, participants = json.dumps(participants))

        elif file_type == "ab":
            narrator = data["narrator"]
            author = data["author"]

            obj = AudiobookFile.objects.create(name=name,
                                                duration= duration,
                                                narrator=narrator,
                                                author = author)
        else:
            #wrong file type
            raise FileTypeException("Filetype invalid value, file type value can only be in [s, p, ab]")
        result["data"] = obj.get_model_as_json()
        result["status"] = 200
        result["success"] = "success"
    except KeyError as e:
        result["data"] = []
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except ValueError as e:
        result["data"] = []
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except FileTypeException as e:
        result["data"] = []
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except Exception as e:
        result["data"] = []
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    
    return JsonResponse(result, status=result["status"])
