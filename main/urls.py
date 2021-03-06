from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()
from views import CreationPlanche
import Constant

urlpatterns = patterns('',

    url(r'^var/', 'main.views.var', name='tab_varietes'),
    url(r'^request/', 'main.serveRequest.serveRequest'),
    url(r'^quiz/', 'main.views.quiz', name='quiz'),
    
    url(r'^edition_planche/', 'main.views.editionPlanche', name='edition_planche'),
   # url(r'^bilan_planche/', 'main.views.bilanPlanche', name='bilan_planche'),

    url(r'^creation_planche/', 
        CreationPlanche.as_view() ,  
        {"appName":Constant.APP_NAME, "appVersion":Constant.APP_VERSION}, 
        name='creation_planche'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^home', 'main.views.home',  name='home'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('home'))),
)
