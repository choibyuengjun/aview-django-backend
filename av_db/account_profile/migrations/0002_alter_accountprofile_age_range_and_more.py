# Generated by Django 5.1.4 on 2025-04-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_profile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountprofile",
            name="age_range",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="accountprofile",
            name="birthyear",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name="accountprofile",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
