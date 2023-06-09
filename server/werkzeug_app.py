#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

##This is the sole function inside of our script. (You can call it anything, we used application for simplicity's sake.) It is decorated with the Request.application method, which tells it to run any code inside of the function in the browser at the location we specify with our development server.
@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

##The run_simple() method runs a server for a one-page application without complications.
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application 
    )
##run_simple() requires three arguments: a hostname (generally localhost, as it is typically used for local development), a port, and an application. This application will be defined in a function somewhere in the file- as we saw before, we named ours application