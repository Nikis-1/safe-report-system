# Generated by Django 5.2.3 on 2025-07-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report_sentiment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
