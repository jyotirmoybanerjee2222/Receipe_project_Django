from django.contrib import admin
from django.urls import path, include
from vege import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.receipes, name="home"),
    path('receipes/', views.receipes, name="receipes"),
    path('delete-receipe/<id>/', views.delete_receipe, name="delete_receipe"),
    path('update-receipe/<id>/', views.update_receipe, name="update_receipe"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),
    path('register/', views.register, name="register"),

    path('api/', include('recipes.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
