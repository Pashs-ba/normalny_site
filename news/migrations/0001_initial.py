# Generated by Django 3.2.8 on 2021-10-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('ru_text', models.TextField()),
                ('en_text', models.TextField()),
            ],
        ),
    ]
