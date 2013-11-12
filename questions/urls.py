from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'questions.views.index', name='questions_index'),
)
