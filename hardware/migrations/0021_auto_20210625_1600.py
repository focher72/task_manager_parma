# Generated by Django 3.1.7 on 2021-06-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0020_auto_20210625_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='active_hardware',
            name='comment',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Комментарий'),
        ),
        migrations.DeleteModel(
            name='HistoricalActive_hardware',
        ),
    ]