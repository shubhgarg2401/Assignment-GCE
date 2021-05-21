def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    test_list1 = a from input
    test_list2 = b from input 
  

    res = sorted(test_list1 + test_list2)
  

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return f'Okay'
    elif request_json and 'message' in request_json:
        return str(res)
    else:
        return f'Hello World!'
