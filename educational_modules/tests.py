from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from educational_modules.models import EducationalModule
from users.models import User


class EducationalModuleTestCase(APITestCase):

    def setUp(self):
        self.maxDiff = None
        self.user = User.objects.create(
            email='test1@mail.com'
        )
        self.user.set_password('test1')

        self.educational_module = EducationalModule.objects.create(name="test",
                                                                   order_number=1,
                                                                   description="TestDescrip",
                                                                   user=self.user
                                                                   )

    def test_educational_module_create(self):
        """
        Тест на создание модуля
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse("educational_modules:modules_create"), {"name": "test1",
                                                                                    "order_number": 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_educational_module_retrieve(self):
        """
        Тест на получение модуля
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse("educational_modules:modules_detail", kwargs={"pk": self.educational_module.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_educational_module_update(self):
        """
        Тест на обновление модуля
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            reverse("educational_modules:modules_update", kwargs={"pk": self.educational_module.pk}),
            {"name": "test1",
             "order_number": 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_educational_module_delete(self):
        """
        Тест на удаление модуля
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse("educational_modules:modules_delete", kwargs={"pk": self.educational_module.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_educational_module_list(self):
        """
        Тест на получение всех модулей
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("educational_modules:modules_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
