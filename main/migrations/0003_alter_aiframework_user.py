# Generated by Django 4.1.7 on 2023-03-31 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_aiframework_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiframework',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aiframework', to=settings.AUTH_USER_MODEL),
        ),
    ]
