# -*- coding: utf-8 -*-
from actions import Archivador
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301



def index_view(request):
    #Archivador('home/index.html', 'index', {})
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def loqueHacemos(request):
    return render_to_response('loquehacemos/lo-que-hacemos.html',
                          context_instance=RequestContext(request))

def uxDesign(request):
    return render_to_response('loquehacemos/ux-design.html',
                          context_instance=RequestContext(request))

def eCommerce(request):
    return render_to_response('loquehacemos/ecommerce.html',
                          context_instance=RequestContext(request))

def webSites(request):
    return render_to_response('loquehacemos/websites.html',
                          context_instance=RequestContext(request))

def marketingOnline(request):
    return render_to_response('loquehacemos/mkt-online.html',
                          context_instance=RequestContext(request))

def appWeb(request):
    return render_to_response('loquehacemos/appWeb.html',
                          context_instance=RequestContext(request))

def portafolio(request):
    return render_to_response('ourWork/nuestro-trabajo.html',
                          context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('home/contacto.html',
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

#REdirects
def blogRedirect(request):
    return redirect('http://blog.phyroserver.com')

def twitterRedirect(request):
    return redirect('https://twitter.com/PhyroServer')

def facebookRedirect(request):
    return redirect('https://www.facebook.com/pages/Phyro-Server-Tehuac%C3%A1n/290497264370516?fref=ts')

def gplusRedirect(request):
    return redirect('https://plus.google.com/+PhyroServerTehuac%C3%A1n/posts')
