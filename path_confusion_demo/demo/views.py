from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    """ Vulnerable profile view allowing path confusion. """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Path Confusion Test</title>
    </head>
    <body>
        <h1>Path Confusion Test</h1>
        <p>Welcome to Your Profile.</p>
        <p><i>Your API Key: a2bc83jc8qncun2j3eoincjqwadnouje</i></p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
