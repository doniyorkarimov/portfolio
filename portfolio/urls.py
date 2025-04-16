from django.urls import  path

from .views import IndexView, AboutView, CredentialsView, WorkDetailView, WorksView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('credentials/', CredentialsView.as_view(), name='credentials'),

    path('works/',WorksView.as_view(), name='works'),
    path('work/<slug:slug>/', WorkDetailView.as_view(), name='work_detail'),

    path('contact/', ContactView.as_view(), name='contact'),

]