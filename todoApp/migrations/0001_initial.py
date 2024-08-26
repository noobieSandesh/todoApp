# Generated by Django 5.1 on 2024-08-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('A', 'Active'), ('C', 'Completed')], default='A', max_length=1)),
            ],
        ),
    ]
