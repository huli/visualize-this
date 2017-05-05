from django.shortcuts import render_to_response

def app(environ, start_response):
   return render_to_response('sometemplate.html')