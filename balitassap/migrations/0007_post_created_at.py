# Generated by Django 5.1.3 on 2024-11-25 12:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("balitassap", "0006_post_category_alter_category_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
