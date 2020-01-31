import datetime

from django.urls import reverse
from rest_framework import status

from traffic_control.models import MountPlan, MountReal

from .test_base_api import TrafficControlAPIBaseTestCase


class MountPlanTests(TrafficControlAPIBaseTestCase):
    def test_get_all_mount_plans(self):
        """
        Ensure we can get all mount plan objects.
        """
        count = 3
        for i in range(count):
            self.__create_test_mount_plan()
        response = self.client.get(reverse("api:mountplan-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), count)

    def test_get_mount_plan_detail(self):
        """
        Ensure we can get one mount plan object.
        """
        mount_plan = self.__create_test_mount_plan()
        response = self.client.get(
            "%s%s/" % (reverse("api:mountplan-list"), str(mount_plan.id))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(mount_plan.id))

    def test_create_mount_plan(self):
        """
        Ensure we can create a new mount plan object.
        """
        data = {
            "type": self.test_type.value,
            "location": self.test_point.ewkt,
            "decision_date": "2020-01-02",
            "lifecycle": self.test_lifecycle.value,
        }
        response = self.client.post(reverse("api:mountplan-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MountPlan.objects.count(), 1)
        mount_plan = MountPlan.objects.first()
        self.assertEqual(mount_plan.type.value, data["type"])
        self.assertEqual(mount_plan.location.ewkt, data["location"])
        self.assertEqual(
            mount_plan.decision_date.strftime("%Y-%m-%d"), data["decision_date"]
        )
        self.assertEqual(mount_plan.lifecycle.value, data["lifecycle"])

    def test_update_mount_plan(self):
        """
        Ensure we can update existing mount plan object.
        """
        mount_plan = self.__create_test_mount_plan()
        data = {
            "type": self.test_type_2.value,
            "location": self.test_point.ewkt,
            "decision_date": "2020-01-03",
            "lifecycle": self.test_lifecycle_2.value,
        }
        response = self.client.put(
            "%s%s/" % (reverse("api:mountplan-list"), str(mount_plan.id)),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MountPlan.objects.count(), 1)
        mount_plan = MountPlan.objects.first()
        self.assertEqual(mount_plan.type.value, data["type"])
        self.assertEqual(mount_plan.location.ewkt, data["location"])
        self.assertEqual(
            mount_plan.decision_date.strftime("%Y-%m-%d"), data["decision_date"]
        )
        self.assertEqual(mount_plan.lifecycle.value, data["lifecycle"])

    def test_delete_mount_plan_detail(self):
        """
        Ensure we can soft-delete one mount plan object.
        """
        mount_plan = self.__create_test_mount_plan()
        response = self.client.delete(
            "%s%s/" % (reverse("api:mountplan-list"), str(mount_plan.id))
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MountPlan.objects.count(), 1)
        deleted_mount_plan = MountPlan.objects.get(id=str(mount_plan.id))
        self.assertEqual(deleted_mount_plan.id, mount_plan.id)
        self.assertEqual(deleted_mount_plan.deleted_by, self.user)
        self.assertTrue(deleted_mount_plan.deleted_at)

    def __create_test_mount_plan(self):
        return MountPlan.objects.create(
            type=self.test_type,
            location=self.test_point,
            decision_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            created_by=self.user,
            updated_by=self.user,
        )


class MountRealTests(TrafficControlAPIBaseTestCase):
    def test_get_all_mount_reals(self):
        """
        Ensure we can get all mount real objects.
        """
        count = 3
        for i in range(count):
            self.__create_test_mount_real()
        response = self.client.get(reverse("api:mountreal-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), count)

    def test_get_mount_real_detail(self):
        """
        Ensure we can get one mount real object.
        """
        mount_real = self.__create_test_mount_real()
        response = self.client.get(
            "%s%s/" % (reverse("api:mountreal-list"), str(mount_real.id))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(mount_real.id))

    def test_create_mount_plan(self):
        """
        Ensure we can create a new mount real object.
        """
        data = {
            "type": self.test_type.value,
            "location": self.test_point.ewkt,
            "installation_date": "2020-01-02",
            "lifecycle": self.test_lifecycle.value,
        }
        response = self.client.post(reverse("api:mountreal-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MountReal.objects.count(), 1)
        mount_real = MountReal.objects.first()
        self.assertEqual(mount_real.type.value, data["type"])
        self.assertEqual(mount_real.location.ewkt, data["location"])
        self.assertEqual(
            mount_real.installation_date.strftime("%Y-%m-%d"),
            data["installation_date"],
        )
        self.assertEqual(mount_real.lifecycle.value, data["lifecycle"])

    def test_update_mount_real(self):
        """
        Ensure we can update existing mount real object.
        """
        mount_real = self.__create_test_mount_real()
        data = {
            "type": self.test_type_2.value,
            "location": self.test_point.ewkt,
            "installation_date": "2020-01-03",
            "lifecycle": self.test_lifecycle_2.value,
        }
        response = self.client.put(
            "%s%s/" % (reverse("api:mountreal-list"), str(mount_real.id)),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MountReal.objects.count(), 1)
        mount_real = MountReal.objects.first()
        self.assertEqual(mount_real.type.value, data["type"])
        self.assertEqual(mount_real.location.ewkt, data["location"])
        self.assertEqual(
            mount_real.installation_date.strftime("%Y-%m-%d"),
            data["installation_date"],
        )
        self.assertEqual(mount_real.lifecycle.value, data["lifecycle"])

    def test_delete_mount_real_detail(self):
        """
        Ensure we can soft-delete one mount real object.
        """
        mount_real = self.__create_test_mount_real()
        response = self.client.delete(
            "%s%s/" % (reverse("api:mountreal-list"), str(mount_real.id))
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MountReal.objects.count(), 1)
        deleted_mount_real = MountReal.objects.get(id=str(mount_real.id))
        self.assertEqual(deleted_mount_real.id, mount_real.id)
        self.assertEqual(deleted_mount_real.deleted_by, self.user)
        self.assertTrue(deleted_mount_real.deleted_at)

    def __create_test_mount_real(self):
        mount_plan = MountPlan.objects.create(
            type=self.test_type,
            location=self.test_point,
            decision_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            created_by=self.user,
            updated_by=self.user,
        )
        return MountReal.objects.create(
            mount_plan=mount_plan,
            type=self.test_type,
            location=self.test_point,
            installation_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            created_by=self.user,
            updated_by=self.user,
        )
