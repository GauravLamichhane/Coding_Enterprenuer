# Generated by Django 5.1.6 on 2025-03-04 12:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_article_timestamp_article_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="publish",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
