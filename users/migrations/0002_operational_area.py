# Generated by Django 2.2.14 on 2020-07-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0017_operational_area"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bypass_operational_area",
            field=models.BooleanField(
                default=False,
                help_text="Disable operational area permission checks for this user.",
                verbose_name="Bypass operational area",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="operational_areas",
            field=models.ManyToManyField(
                blank=True, related_name="users", to="traffic_control.OperationalArea"
            ),
        ),
    ]
