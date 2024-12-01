from django.urls import path, include
from .views import RawMaterialUploadView, MenuApiView

urlpatterns = [
    path("save-excel-data/", RawMaterialUploadView.as_view()),
    
    path('create-menu/',MenuApiView.as_view())

]