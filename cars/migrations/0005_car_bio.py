# Generated by Django 5.0.4 on 2024-05-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
