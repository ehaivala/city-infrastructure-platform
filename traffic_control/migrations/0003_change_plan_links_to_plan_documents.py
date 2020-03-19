# Generated by Django 2.2.10 on 2020-03-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0002_add_legacy_fields"),
    ]

    operations = [
        migrations.RemoveField(model_name="barrierplan", name="plan_link",),
        migrations.RemoveField(model_name="mountplan", name="plan_link",),
        migrations.RemoveField(model_name="roadmarkingplan", name="plan_link",),
        migrations.RemoveField(model_name="signpostplan", name="plan_link",),
        migrations.RemoveField(model_name="trafficlightplan", name="plan_link",),
        migrations.RemoveField(model_name="trafficsignplan", name="plan_link",),
        migrations.AddField(
            model_name="barrierplan",
            name="plan_document",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Plan document"
            ),
        ),
        migrations.AddField(
            model_name="mountplan",
            name="plan_document",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Plan document"
            ),
        ),
        migrations.AddField(
            model_name="roadmarkingplan",
            name="plan_document",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Plan document"
            ),
        ),
        migrations.AddField(
            model_name="signpostplan",
            name="plan_document",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Plan document"
            ),
        ),
        migrations.AddField(
            model_name="trafficlightplan",
            name="plan_document",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Plan document"
            ),
        ),
        migrations.AddField(
            model_name="trafficsignplan",
            name="plan_document",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="Plan document"
            ),
        ),
    ]