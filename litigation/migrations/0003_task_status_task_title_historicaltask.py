# Generated by Django 5.2.4 on 2025-07-27 13:20

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litigation', '0002_alter_task_priority'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Open'), (10, 'In Progress'), (20, 'Completed'), (100, 'Closed')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Title 1', max_length=40),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('title', models.CharField(max_length=40)),
                ('priority', models.PositiveSmallIntegerField(choices=[(10, 'Low'), (20, 'Medium'), (30, 'High'), (40, 'Urgent')], default=20, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Open'), (10, 'In Progress'), (20, 'Completed'), (100, 'Closed')], default=0, null=True)),
                ('description', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical task',
                'verbose_name_plural': 'historical tasks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
