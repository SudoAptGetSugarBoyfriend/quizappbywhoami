"""DjangoQuiz URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static
from Quiz import views
from rest_framework_simplejwt import views as view
from Quiz.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('quizapi/', views.QuizApiList.as_view(), name='quizapi'),
    path('userapi/', views.UserApiList.as_view(), name='userapi'),
    path('api-token-auth/', view.TokenObtainPairView.as_view(), name='api-token-auth'),
    path('api/token/refresh/', view.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('registerapi/', RegisterUserAPIView.as_view()),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
