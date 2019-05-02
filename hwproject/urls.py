from django.contrib import admin
from django.urls import path
import postapp.views
import userapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', postapp.views.index, name="index"),
    path('<int:post_id>/', postapp.views.detail, name="detail"),
    path('<int:post_id>/delet', postapp.views.delet, name="delet"),
    path('new/', postapp.views.new, name="new"),
    path('<int:post_id>/update/', postapp.views.update, name="update"),
    path('signup/', userapp.views.signup, name="signup"),
    path('login/', userapp.views.login, name="login"),
    path('logout/', userapp.views.logout, name="logout"),
    
]
