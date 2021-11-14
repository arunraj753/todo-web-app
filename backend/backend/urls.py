from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts import views as account_views
from todo.router import router as todo_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', account_views.LoginView.as_view()),
    path('register', account_views.UserRegistrationView.as_view()),
    path('profile', account_views.Profile.as_view()),
    path('', include(todo_router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
