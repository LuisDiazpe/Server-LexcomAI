# Generated by Django 5.0.3 on 2024-03-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='progress_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='search_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='search_plan',
            field=models.CharField(choices=[('free', 'Free'), ('standard', 'Standard'), ('business', 'Business'), ('premium', 'Premium')], default='free', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='searches_allowed',
            field=models.IntegerField(default=2),
        ),
    ]
