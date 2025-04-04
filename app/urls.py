from django.urls import path
from . import views

urlpatterns = [
    path('list',views.list),
    path('update/<int:id>',views.update),
    path('filterr',views.filterr,name='list_course'),
    path('detail/<int:id>',views.detail,name='detail_1')
]
