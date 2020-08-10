# Generated by Django 2.2 on 2020-08-10 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_conteststandingsholder'),
    ]

    operations = [
        migrations.CreateModel(
            name='EjudgeRegisterApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('secret', models.TextField()),
                ('login', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='standings',
            name='js_for_contest_mark',
            field=models.TextField(blank=True, default='var newCalculateContestMark = function(\n    total_scores,       // двумерный массив пар балла и времени сдачи задач пользователями\n    user_id,            // номер пользователя\n    contest_info        // информация о контесте\n) {\n    return useOldContestMark(total_scores, user_id)\n};'),
        ),
        migrations.CreateModel(
            name='EjudgeRegisterApiGroupAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_login', models.BooleanField(default=True)),
                ('ejudge_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='courses.EjudgeRegisterApi')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registers', to='courses.ParticipantsGroup')),
            ],
        ),
        migrations.CreateModel(
            name='EjudgeRegisterApiContestAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.IntegerField()),
                ('ejudge_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contests', to='courses.EjudgeRegisterApi')),
            ],
        ),
    ]
