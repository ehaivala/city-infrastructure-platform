import datetime

import pytest
from django.urls import reverse
from rest_framework import status

from traffic_control.models import SignpostPlan, SignpostReal

from .factories import get_api_client, get_signpost_plan, get_signpost_real
from .test_base_api import point_location_test_data, TrafficControlAPIBaseTestCase


@pytest.mark.django_db
@pytest.mark.parametrize(
    "location,query_location,expected", point_location_test_data,
)
def test_filter_signpost_plan_location(location, query_location, expected):
    """
    Ensure that filtering with location is working correctly.
    """
    api_client = get_api_client()

    get_signpost_plan(location)
    response = api_client.get(
        reverse("api:signpostplan-list"), {"location": query_location.ewkt}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == expected


class SignpostPlanTests(TrafficControlAPIBaseTestCase):
    def test_get_all_signpost_plans(self):
        """
        Ensure we can get all signpost plan objects.
        """
        count = 3
        for i in range(count):
            self.__create_test_signpost_plan()
        response = self.client.get(reverse("api:signpostplan-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), count)

    def test_get_signpost_plan_detail(self):
        """
        Ensure we can get one signpost plan object.
        """
        signpost_plan = self.__create_test_signpost_plan()
        response = self.client.get(
            reverse("api:signpostplan-detail", kwargs={"pk": signpost_plan.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(signpost_plan.id))

    def test_create_signpost_plan(self):
        """
        Ensure we can create a new signpost plan object.
        """
        data = {
            "code": self.test_code.id,
            "location": self.test_point.ewkt,
            "decision_date": "2020-01-02",
            "lifecycle": self.test_lifecycle.value,
            "owner": self.test_owner,
        }
        response = self.client.post(
            reverse("api:signpostplan-list"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SignpostPlan.objects.count(), 1)
        signpost_plan = SignpostPlan.objects.first()
        self.assertEqual(signpost_plan.code.id, data["code"])
        self.assertEqual(signpost_plan.location.ewkt, data["location"])
        self.assertEqual(
            signpost_plan.decision_date.strftime("%Y-%m-%d"), data["decision_date"]
        )
        self.assertEqual(signpost_plan.lifecycle.value, data["lifecycle"])

    def test_update_signpost_plan(self):
        """
        Ensure we can update existing signpost plan object.
        """
        signpost_plan = self.__create_test_signpost_plan()
        data = {
            "code": self.test_code_2.id,
            "location": self.test_point.ewkt,
            "decision_date": "2020-01-03",
            "lifecycle": self.test_lifecycle_2.value,
            "owner": self.test_owner,
        }
        response = self.client.put(
            reverse("api:signpostplan-detail", kwargs={"pk": signpost_plan.id}),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SignpostPlan.objects.count(), 1)
        signpost_plan = SignpostPlan.objects.first()
        self.assertEqual(signpost_plan.code.id, data["code"])
        self.assertEqual(signpost_plan.location.ewkt, data["location"])
        self.assertEqual(
            signpost_plan.decision_date.strftime("%Y-%m-%d"), data["decision_date"]
        )
        self.assertEqual(signpost_plan.lifecycle.value, data["lifecycle"])

    def test_delete_signpost_plan_detail(self):
        """
        Ensure we can soft-delete one signpost plan object.
        """
        signpost_plan = self.__create_test_signpost_plan()
        response = self.client.delete(
            reverse("api:signpostplan-detail", kwargs={"pk": signpost_plan.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SignpostPlan.objects.count(), 1)
        deleted_signpost_plan = SignpostPlan.objects.get(id=str(signpost_plan.id))
        self.assertEqual(deleted_signpost_plan.id, signpost_plan.id)
        self.assertEqual(deleted_signpost_plan.deleted_by, self.user)
        self.assertTrue(deleted_signpost_plan.deleted_at)

    def __create_test_signpost_plan(self):
        return SignpostPlan.objects.create(
            code=self.test_code,
            location=self.test_point,
            decision_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            created_by=self.user,
            updated_by=self.user,
        )


@pytest.mark.django_db
@pytest.mark.parametrize(
    "location,query_location,expected", point_location_test_data,
)
def test_filter_signpost_reals_location(location, query_location, expected):
    """
    Ensure that filtering with location is working correctly.
    """
    api_client = get_api_client()

    get_signpost_real(location)
    response = api_client.get(
        reverse("api:signpostreal-list"), {"location": query_location.ewkt}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == expected


class SignPostRealTests(TrafficControlAPIBaseTestCase):
    def test_get_all_signpost_reals(self):
        """
        Ensure we can get all sign post real objects.
        """
        count = 3
        for i in range(count):
            self.__create_test_signpost_real()
        response = self.client.get(reverse("api:signpostreal-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), count)

    def test_get_signpost_real_detail(self):
        """
        Ensure we can get one signpost real object.
        """
        signpost_real = self.__create_test_signpost_real()
        response = self.client.get(
            reverse("api:signpostreal-detail", kwargs={"pk": signpost_real.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(signpost_real.id))

    def test_create_signpost_plan(self):
        """
        Ensure we can create a new signpost real object.
        """
        data = {
            "code": self.test_code.id,
            "location": self.test_point.ewkt,
            "installation_date": "2020-01-02",
            "lifecycle": self.test_lifecycle.value,
            "owner": self.test_owner,
        }
        response = self.client.post(
            reverse("api:signpostreal-list"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SignpostReal.objects.count(), 1)
        signpost_real = SignpostReal.objects.first()
        self.assertEqual(signpost_real.code.id, data["code"])
        self.assertEqual(signpost_real.location.ewkt, data["location"])
        self.assertEqual(
            signpost_real.installation_date.strftime("%Y-%m-%d"),
            data["installation_date"],
        )
        self.assertEqual(signpost_real.lifecycle.value, data["lifecycle"])

    def test_update_signpost_real(self):
        """
        Ensure we can update existing signpost real object.
        """
        signpost_real = self.__create_test_signpost_real()
        data = {
            "code": self.test_code_2.id,
            "location": self.test_point.ewkt,
            "installation_date": "2020-01-03",
            "lifecycle": self.test_lifecycle_2.value,
            "owner": self.test_owner,
        }
        response = self.client.put(
            reverse("api:signpostreal-detail", kwargs={"pk": signpost_real.id}),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SignpostReal.objects.count(), 1)
        signpost_real = SignpostReal.objects.first()
        self.assertEqual(signpost_real.code.id, data["code"])
        self.assertEqual(signpost_real.location.ewkt, data["location"])
        self.assertEqual(
            signpost_real.installation_date.strftime("%Y-%m-%d"),
            data["installation_date"],
        )
        self.assertEqual(signpost_real.lifecycle.value, data["lifecycle"])

    def test_delete_signpost_real_detail(self):
        """
        Ensure we can soft-delete one signpost real object.
        """
        signpost_real = self.__create_test_signpost_real()
        response = self.client.delete(
            reverse("api:signpostreal-detail", kwargs={"pk": signpost_real.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SignpostReal.objects.count(), 1)
        deleted_signpost_real = SignpostReal.objects.get(id=str(signpost_real.id))
        self.assertEqual(deleted_signpost_real.id, signpost_real.id)
        self.assertEqual(deleted_signpost_real.deleted_by, self.user)
        self.assertTrue(deleted_signpost_real.deleted_at)

    def __create_test_signpost_real(self):
        signpost_plan = SignpostPlan.objects.create(
            code=self.test_code,
            location=self.test_point,
            decision_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            created_by=self.user,
            updated_by=self.user,
        )
        return SignpostReal.objects.create(
            signpost_plan=signpost_plan,
            code=self.test_code,
            location=self.test_point,
            installation_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            created_by=self.user,
            updated_by=self.user,
        )
