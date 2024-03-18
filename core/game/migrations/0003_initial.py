# Generated by Django 5.0.3 on 2024-03-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0002_delete_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.PositiveIntegerField(unique=True)),
                ('player1', models.CharField(max_length=100)),
                ('player2', models.CharField(max_length=100)),
                ('player1wins', models.PositiveIntegerField(default=0)),
                ('player2wins', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]