# Generated by Django 3.2.3 on 2023-07-23 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursebuilder', '0007_course_price_orderdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursebuilder.course')),
            ],
        ),
        migrations.CreateModel(
            name='MembersName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('semester', models.PositiveIntegerField(default=3)),
                ('link', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]