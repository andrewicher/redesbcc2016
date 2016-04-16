from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(request):
    #Check to see if 
    if 'id' in request.COOKIES:
        cookie_id = request.COOKIES['id']
        context = {'cookie_id' : cookie_id}
        return render(request, 'adserver/index.html', context)
    else:
        resp = render(request, 'adserver/index.html')
        resp.set_cookie('id', 'product_99')
        return resp

def productPage(request, product_id):

    return HttpResponse("You're looking at product %s." % product_id)
