# Generated by Django 4.2.3 on 2023-07-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursebuilder', '0002_assignment_labs_notes_ppt_delete_coursefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to='coursebuilder.userprofile'),
        ),
    ]
