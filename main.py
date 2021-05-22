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
    
    
    data1='message1' in request.get_json()      #storing the json payload dictionary in data1
    data2='message2' in request.get_json()      #storing the json payload dictionary in data
    
    list1=json.loads(data1)                     #converting the json array into python list
    list2=json.loads(data2)
    
    
     
  

    res = sorted(list1 + list2)                 #combining the two lists and then sorting them using the sorted() method
  

    request_json = request.get_json()               # giving the request.get_json() function a name
    if request.args and 'message' in request.args:      #checking for arguments via the http url
        return f'Try again using the JSON payload'      # putting out a message
    elif request_json and 'message' in request_json:    #checking for json payload input
        return str(res)                                 #the final string
    else:
        return f'Invalid Input, Try Again!'
