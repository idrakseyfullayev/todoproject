from django.urls import path, include
from todo import views

app_name = "todo"

urlpatterns= [
    path('index', views.IndexView.as_view(), name="index"),
    path('work_update/<int:id>', views.update_work, name="work_update"),
    path('start_time_update/<int:id>', views.update_start_time, name="start_time_update" ),
    path('end_time_update/<int:id>', views.update_end_time, name = "end_time_update"),
    path('delete/<int:id>', views.delete_, name="delete"),
]

