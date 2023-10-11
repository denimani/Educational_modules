from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from educational_modules.models import EducationalModule
from educational_modules.serializers import EducationalModuleSerializer


class EducationalModuleListView(ListAPIView):
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer


class EducationalModuleCreateView(CreateAPIView):
    serializer_class = EducationalModuleSerializer


class EducationalModuleRetrieveView(RetrieveAPIView):
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer


class EducationalModuleUpdateView(UpdateAPIView):
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer


class EducationalModuleDestroyView(DestroyAPIView):
    queryset = EducationalModule.objects.all()
