# Generated by Django 4.2.1 on 2023-05-06 17:29

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogmodel",
            name="content",
            field=froala_editor.fields.FroalaField(),
        ),
    ]
