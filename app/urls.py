from django.urls import path, include

from app import views
urlpatterns = [
    # HOME PAGE
    path('', views.home),

    # TIMELINE SUB-PAGE
    path('timeline/', views.timeline),

    # ABOUT
    path('about/', views.about),

    # ABOUT-DETALHES
    path('aboutDetalhes1/', views.aboutDetalhes1),
    path('aboutDetalhes2/', views.aboutDetalhes2),
    path('aboutDetalhes3/', views.aboutDetalhes3),

    # ABOUT-US
    path('aboutUs/', views.aboutUs),
    
    # PRODUCTS SUB-PAGES
    path('products1/', views.products1),
    path('products2/', views.products2),
    path('products3/', views.products3),

    # PARE SUB-PAGE
    path('pare/', views.pare),

    # COMMON-QUESTIONS SUB-PAGE
    path('common/', views.common),

    # DETALHES SUB-PAGE
    path('detalhes/', views.detalhes),

    # PRICING SUB-PAGE
    path('pricing/', views.pricing),

    # LOGIN SUB-PAGE
    path('login/', views.login),

    # user-index SUB-PAGE
    path('userIndex/', views.userIndex),
]