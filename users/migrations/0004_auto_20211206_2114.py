# Generated by Django 3.2.9 on 2021-12-06 18:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211205_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
