import json
from django.http import JsonResponse
from django.views import View
from .models import *
from django.views.decorators.http import require_http_methods
from .AudioFileInterface import FileTypeException, check_participant_strngth
# Create your views here.

'''
Module views.py will contains
Read
Update
delete
apis for audiofile app
'''

@require_http_methods(["GET"])
def read_audio_file(request, file_type, file_id =None):
    '''
    GET api which will fetch data on basis of follwing conditions
    -The route “<audioFileType>/<audioFileID>” will return the specific audio file
    -The route “<audioFileType>” will return all the audio files of that type
    Fetch either specific data of audiofile using id
    or return all data of asked file type
    '''
    result = dict()
    try:
        if not file_type:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")

        if file_type == "s":
            #fetch all song objects
            obj = SongFile.objects.all()
        elif file_type == "p":
            obj = PodcastFile.objects.all()
        elif file_type == "ab":
            obj = AudiobookFile.objects.all()
        else:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")

        if file_id:
            obj = obj.filter(pk=file_id)

        result["data"] = [object.get_model_as_json() for object in obj] 
        result["status"] = 200
        result["success"] = "success"
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

@require_http_methods(["DELETE"])
def delete_audio_file(request, file_type, file_id):
    '''
    Api will delete the specific object file from db
    '''
    result = dict()
    try:
        if not file_type:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")
        if not file_id:
            raise ValueError("No file id provided")
        if file_type == "s":
            #fetch all song objects
            SongFile.objects.get(pk=file_id).delete()
        elif file_type == "p":
            PodcastFile.objects.get(pk=file_id).delete()
        elif file_type == "ab":
            AudiobookFile.objects.get(pk=file_id).delete()
        else:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")
        result["status"] = 200
        result["success"] = "success"

    except ValueError as e:
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except FileTypeException as e:
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except Exception as e:
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    return JsonResponse(result, status=result["status"])


@require_http_methods(["PUT"])
def update_audio_file(request, file_type, file_id):
    '''
    Api will update the specific object file from db
    '''
    result = dict()
    try:
        if not file_type:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")
        if not file_id:
            raise ValueError("No file id provided")

        data = json.loads(request.body)
        name = data["name"]
        duration = data["duration"]
        if file_type == "s":
            #fetch all song objects
            obj = SongFile.objects.get(pk=file_id)
            obj.name = name
            obj.duration = duration
            obj.save()
        
        elif file_type == "p":
            obj = PodcastFile.objects.get(pk=file_id)
            host = data["host"]
            participants = data.get("participants",[])#optional
            if len(participants) > 10:
                raise ValueError("participants cant be more than 10")
            for word in participants:
                check_participant_strngth(word)
            obj.name = name
            obj.host = host
            obj.participants = json.dumps(participants)
            obj.duration = duration
            obj.save()
        
        elif file_type == "ab":
            obj = AudiobookFile.objects.get(pk=file_id)
            narrator = data["narrator"]
            author = data["author"]
            obj.name = name
            obj.duration = duration
            obj.author = author
            obj.narrator = narrator
            obj.save()
    
        else:
            raise FileTypeException("Filetype cant be None.File type value can only be in [s, p, ab]")

        result["data"] = obj.get_model_as_json()
        result["status"] = 200
        result["success"] = "success"

    except ValueError as e:
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except FileTypeException as e:
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    except Exception as e:
        result["error_reason"] = str(e)
        result["result"] = "failure"
        result["status"] = 400
    return JsonResponse(result, status=result["status"])