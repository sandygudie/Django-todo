# Generated by Django 4.2.5 on 2024-06-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_alter_todo_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]