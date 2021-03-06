# Generated by Django 2.2.14 on 2020-09-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0019_remove_traffic_sign_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="barrierplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="barrierplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="barrierreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="barrierreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="mountplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="mountplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="mountreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="mountreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="operationalarea",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="operationalarea",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="signpostplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="signpostplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="signpostreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="signpostreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="trafficlightplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="trafficlightplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AddField(
            model_name="trafficlightreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AddField(
            model_name="trafficlightreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterField(
            model_name="additionalsignplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AlterField(
            model_name="additionalsignplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterField(
            model_name="additionalsignreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AlterField(
            model_name="additionalsignreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterField(
            model_name="roadmarkingplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AlterField(
            model_name="roadmarkingplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterField(
            model_name="roadmarkingreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AlterField(
            model_name="roadmarkingreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterField(
            model_name="trafficsignplan",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AlterField(
            model_name="trafficsignplan",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterField(
            model_name="trafficsignreal",
            name="source_id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=64,
                null=True,
                verbose_name="Source id",
            ),
        ),
        migrations.AlterField(
            model_name="trafficsignreal",
            name="source_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=254,
                null=True,
                verbose_name="Source name",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="additionalsignplan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="additionalsignreal",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="barrierplan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="barrierreal",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="mountplan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="mountreal",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="operationalarea",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="plan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="signpostplan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="signpostreal",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="trafficlightplan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="trafficlightreal",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="trafficsignplan",
            unique_together={("source_name", "source_id")},
        ),
        migrations.AlterUniqueTogether(
            name="trafficsignreal",
            unique_together={("source_name", "source_id")},
        ),
    ]
