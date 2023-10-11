from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from models import EducationalModule
from serializers import EducationalModuleSerializer


class EducationalModuleListCreateView(CreateAPIView):
    serializer_class = EducationalModuleSerializer


class EducationalModuleRetrieveView(RetrieveAPIView):
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer


class EducationalModuleUpdateView(UpdateAPIView):
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer


class EducationalModuleDestroyView(DestroyAPIView):
    queryset = EducationalModule.objects.all()
