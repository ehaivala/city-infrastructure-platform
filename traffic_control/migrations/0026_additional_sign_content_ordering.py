# Generated by Django 2.2.14 on 2020-09-17 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0025_update_operational_area"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="additionalsigncontentplan",
            options={
                "ordering": ("parent", "order"),
                "verbose_name": "Additional Sign Content Plan",
                "verbose_name_plural": "Additional Sign Content Plans",
            },
        ),
        migrations.AlterModelOptions(
            name="additionalsigncontentreal",
            options={
                "ordering": ("parent", "order"),
                "verbose_name": "Additional Sign Content Real",
                "verbose_name_plural": "Additional Sign Content Reals",
            },
        ),
    ]