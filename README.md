# AudioPlayer
AudioPlayer CRUD Apis

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Upload Audio File
http://127.0.0.1:8000/audiofile/create/
'''
Single Endpoint for all 3 kinds of file Each request will have all metadictionary and
each file type will use its needed arguments from the request body..
'''
{
    "file_type":"ab",
    "name":"pschology of money",
    "duration":59000,
    "host":"",
    "participants":[],
    "narrator":"Morgan",
    "author":"Morgan housel"
}

||||||||||||||||||||||||||||||||||||||||||||||||||||||
GET Read Audio File
urls:
        http://127.0.0.1:8000/audiofile/file/ab/
        http://127.0.0.1:8000/audiofile/file/ab/1
'''
Fetch audio file which can be specific file using id or can fetch all files for given file type
'''

|||||||||||||||||||||||||||||||||||||||||||||||||||||||

DEL Delete speific file
url : http://127.0.0.1:8000/audiofile/remove/ab/2
Deletes the given file id for file type from backend

|||||||||||||||||||||||||||||||||||||||||||||||||||||||
PUT Update specific file
url : http://127.0.0.1:8000/audiofile/update/ab/1
Given the file id and filetype This updates the existing object with new values provided. request body works in the same way as of upload

{
    "name":"mind",
    "duration":300,
    "host":"maty",
    "participants":[],
    "author":"konkan",
    "narrator":"koikl"
}
