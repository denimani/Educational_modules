from django.urls import path

from educational_modules.apps import EducationalModulesConfig
from educational_modules.views import EducationalModuleListView, EducationalModuleCreateView, \
    EducationalModuleRetrieveView, EducationalModuleUpdateView, EducationalModuleDestroyView

app_name = EducationalModulesConfig.name

urlpatterns = [
    path('educational_modules/', EducationalModuleListView.as_view(), name='modules_list'),
    path('educational_modules/create/', EducationalModuleCreateView.as_view(), name='modules_create'),
    path('educational_modules/<int:pk>/update/', EducationalModuleUpdateView.as_view(), name='modules_update'),
    path('educational_modules/<int:pk>/detail/', EducationalModuleRetrieveView.as_view(), name='modules_detail'),
    path('educational_modules/<int:pk>/delete/', EducationalModuleDestroyView.as_view(), name='modules_delete')
]
