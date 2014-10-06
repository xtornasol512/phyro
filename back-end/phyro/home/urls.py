from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns=patterns('home.views',
    #HOME
    url(r'^$','index_view', name='vista_principal'),
    #estaticos
    url(r'^humans.txt$', TemplateView.as_view(template_name='statics/humans.txt', content_type='text/plain; charset=utf-8')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='statics/robots.txt', content_type='text/plain; charset=utf-8')),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='statics/sitemap.xml', content_type='application/xml; charset=utf-8')),
    #secciones
    url(r'^lo-que-hacemos/$', 'loqueHacemos'),
    url(r'^lo-que-hacemos/ux-ui-design/$', 'uxDesign'),
    url(r'^lo-que-hacemos/ecommerce/$', 'eCommerce'),
    url(r'^lo-que-hacemos/websites/$', 'webSites'),
    url(r'^lo-que-hacemos/marketing-online/$', 'marketingOnline'),
    url(r'^lo-que-hacemos/aplicaciones-web/$', 'appWeb'),
    #secciones
    url(r'^nuestro-trabajo/$', 'portafolio'),
    url(r'^contacto/$', 'contacto'),
    url(r'^about-us/$', 'aboutUS'),
    url(r'^expo-guadalajara/$', 'landing'),

    #Equipo y sus paginas.
    url(r'^team/$', 'team'),
    url(r'^alen/$', 'alen'),
    url(r'^jesus/$', 'chucho'),
    url(r'^luciano/$', 'luciano'),
    #REDirects
    url(r'^blog/$', 'blogRedirect'),
    url(r'^facebook/$', 'facebookRedirect'),
    url(r'^twitter/$', 'twitterRedirect'),
    url(r'^g\+/$', 'gplusRedirect'),
    url(r'^map/$', 'blogRedirect'),
    url(r'^fcq/$', 'blogRedirect'),

)