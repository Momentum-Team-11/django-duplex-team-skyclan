# Generated by Django 4.0.3 on 2022-03-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_card_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='correct_count',
            field=models.IntegerField(default=0),
        ),
    ]
