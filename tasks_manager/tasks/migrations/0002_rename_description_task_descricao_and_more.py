# Generated by Django 4.2.3 on 2023-07-07 02:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='task',
            name='criada_em',
        ),
        migrations.AddField(
            model_name='task',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
