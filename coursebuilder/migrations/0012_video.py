# Generated by Django 3.2.3 on 2023-07-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursebuilder', '0011_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video_file', models.FileField(upload_to='videos/%y')),
                ('description', models.TextField()),
            ],
        ),
    ]
