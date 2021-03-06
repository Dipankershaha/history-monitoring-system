# Generated by Django 3.1.4 on 2021-04-01 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField()),
                ('search_date', models.DateTimeField(auto_now_add=True)),
                ('search_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-search_date'],
            },
        ),
    ]
