# Generated by Django 2.2.6 on 2019-11-17 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('changed_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.TextField()),
                ('body', models.TextField()),
                ('reporter_email', models.EmailField(max_length=254)),
                ('reporter_name', models.TextField()),
                ('state', models.CharField(choices=[('NE', 'New'), ('PR', 'Processed'), ('SL', 'Solved'), ('CL', 'Closed')], default='NE', max_length=2)),
                ('time_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.TimeState')),
            ],
        ),
        migrations.CreateModel(
            name='SupportOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
                ('time_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.TimeState')),
            ],
        ),
    ]
