"""general URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from core.views import IndexView,IndexSetPageView, set_site, ContactView, AboutView, FaqView, SubscribeView

app_name = 'core'

urlpatterns = [
    path('', IndexSetPageView.as_view(), name='index-set'),
    path('<str:domain>/', IndexView.as_view(), name='index'),
    path('<str:domain>/elaqe/', ContactView.as_view(), name='contact'),
    path('<str:domain>/haqqimizda/', AboutView.as_view(), name='about'),
    path('<str:domain>/faq/', FaqView.as_view(), name='faq'),
    path('<str:domain>/set_site/<int:id>/', set_site, name='set_site'),
    path('<str:domain>/subscribe/', SubscribeView.as_view(), name='subscribe'),
]