from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns=patterns('phyrosite.home.views',
    #HOME
    url(r'^$','index_view', name='vista_principal'),
    #estaticos
    url(r'^humans.txt$', TemplateView.as_view(template_name='home/humans.txt', content_type='text/plain; charset=utf-8')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='home/robots.txt', content_type='text/plain; charset=utf-8')),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='home/sitemap.xml', content_type='application/xml; charset=utf-8')),
    #secciones
    url(r'^lo-que-hacemos/$', 'loqueHacemos'),
    url(r'^lo-que-hacemos/ux-ui-design/$', 'ux-Design'),
    url(r'^lo-que-hacemos/ecommerce/$', 'eCommerce'),
    url(r'^lo-que-hacemos/websites/$', 'webSites'),
    url(r'^lo-que-hacemos/marketing-online/$', 'marketingOnline'),
    url(r'^lo-que-hacemos/aplicaciones-web/$', 'appWeb'),
    #secciones
    url(r'^nuestro-trabajo/$', 'portafolio'),
    url(r'^contacto/$', 'contacto'),
    url(r'^about-us/$', 'aboutUS'),
    url(r'^blog/$', 'blogRedirect'),





)