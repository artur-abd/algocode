# Generated by Django 3.2.6 on 2022-06-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0036_auto_20210817_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoleChudesGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('guess_cost', models.IntegerField()),
                ('miss_penalty', models.IntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pole_chudes_games', to='courses.contest')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pole_chudes_games', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='PoleChudesWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('hint', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='courses.polechudesgame')),
            ],
        ),
        migrations.CreateModel(
            name='PoleChudesTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('score', models.IntegerField()),
                ('wordId', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='courses.polechudesgame')),
            ],
        ),
        migrations.CreateModel(
            name='PoleChudesParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pole_chudes_participants', to='courses.participant')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='courses.polechudesteam')),
            ],
        ),
        migrations.CreateModel(
            name='PoleChudesLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordId', models.IntegerField()),
                ('letter', models.IntegerField()),
                ('score', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guesses', to='courses.polechudesteam')),
            ],
        ),
        migrations.CreateModel(
            name='PoleChudesGuess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordId', models.IntegerField()),
                ('guessed', models.BooleanField()),
                ('score', models.IntegerField(default=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='courses.polechudesteam')),
            ],
        ),
    ]