from django.urls import path
from . import views


urlpatterns = [
     path('', views.dashboards),
 ]
  



# from django.urls import path
# from .views import dashboards, update_post_status

# urlpatterns = [
#     path('dashboards/', dashboards, name='dashboards'),
#     path('update-post-status/', update_post_status, name='update_post_status'),
# ]
