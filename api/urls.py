from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('audio-detail/<str:pk>', views.audioDetail, name="audio-detail"),
	path('audio-detail-start', views.audioDetailWithStartTime, name="audio-detail-start"),
	path('audio-create/', views.audioCreate, name="audio-create"),

	path('audio-update/<str:pk>', views.audioUpdate, name="audio-update"),
	path('audio-delete/<str:pk>', views.audioDelete, name="audio-delete"),
]
