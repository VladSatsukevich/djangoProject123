"""djangoProject123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about, contacts, news, store, cart, checkout, updateItem, processOrder
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url('about', about, name='about'),
    url('contacts', contacts, name='contacts'),
    url('news', news, name='news'),
    url('store', store, name="store"),
    url('cart', cart, name="cart"),
    url('checkout', checkout, name="checkout"),
    url('update_item', updateItem, name="update_item"),
    url('process_order', processOrder, name="process_order"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)