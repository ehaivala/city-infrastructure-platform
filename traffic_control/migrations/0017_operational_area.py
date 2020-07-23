# Generated by Django 2.2.14 on 2020-07-28 10:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("traffic_control", "0016_mount_type_finnish_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="OperationalArea",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Name")),
                (
                    "area",
                    django.contrib.gis.db.models.fields.PolygonField(
                        srid=3879, verbose_name="Area"
                    ),
                ),
            ],
            options={
                "verbose_name": "Operational area",
                "verbose_name_plural": "Operational areas",
            },
        ),
        migrations.CreateModel(
            name="GroupOperationalArea",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "areas",
                    models.ManyToManyField(
                        blank=True,
                        related_name="groups",
                        to="traffic_control.OperationalArea",
                    ),
                ),
                (
                    "group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="operational_area",
                        to="auth.Group",
                    ),
                ),
            ],
            options={
                "verbose_name": "Group operational area",
                "verbose_name_plural": "Group operational areas",
            },
        ),
    ]
