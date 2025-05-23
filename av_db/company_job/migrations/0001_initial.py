# Generated by Django 5.1.4 on 2025-05-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CompanyJob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "company_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("job_title", models.CharField(blank=True, max_length=200, null=True)),
                ("post_url", models.URLField(blank=True, null=True)),
                ("posted_at", models.DateTimeField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "company_job",
            },
        ),
    ]
