# Generated by Django 4.2.1 on 2023-10-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0065_course_algocode_url_standings_disable_contest_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
