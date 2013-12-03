from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'questions.views.index', name='questions_index'),
    url(r'^add/$', 'questions.views.add', name='questions_add'),
    url(r'^answer/(\d+)/$', 'questions.views.answer', name='questions_answer'),
)
