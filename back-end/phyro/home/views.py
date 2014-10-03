# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301

def index_view(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def loqueHacemos(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def uxDesign(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def eCommerce(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def webSites(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def marketingOnline(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def appWeb(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def portafolio(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def aboutUS(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def team(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def alen(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def chucho(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def luciano(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def landing(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))