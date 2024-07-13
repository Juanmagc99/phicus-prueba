# Generated by Django 5.0.7 on 2024-07-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('board', models.CharField(default='         ', max_length=9)),
                ('last_player', models.CharField(blank=True, choices=[('X', 'Player X'), ('O', 'Player O')], max_length=1, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('winner', models.CharField(blank=True, choices=[('X', 'Player X'), ('O', 'Player O'), ('T', 'Tie')], max_length=1, null=True)),
            ],
        ),
    ]
