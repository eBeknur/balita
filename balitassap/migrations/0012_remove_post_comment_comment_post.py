# Generated by Django 5.1.3 on 2024-11-25 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("balitassap", "0011_rename_phone_comment_website"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="comment",
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="balitassap.post",
            ),
        ),
    ]
