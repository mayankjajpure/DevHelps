# Generated by Django 4.2.1 on 2023-05-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_blogmodel_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogmodel",
            name="subtitle",
            field=models.CharField(default="Test", max_length=100),
            preserve_default=False,
        ),
    ]