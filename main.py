import json

#json library comes pre-installed with python, so no need to include it in the requirments.txt file

def assignment_gce(request):
    
    #Creating a function by the name of assignment_gce which will alos be used as an entry point to the function.
    
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    
    
    data1='message1' in request.get_json()      #storing the json payload dictonary
    data2='message2' in request.get_json()
    
    list1=json.loads(data1)
    list2=json.loads(data2)
    
    
     
  

    res = sorted(list1 + list2)
  

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return f'Try again using the JSON payload'
    elif request_json and 'message' in request_json:
        return str(res)
    else:
        return f'Invalid Input, Try Again!'
