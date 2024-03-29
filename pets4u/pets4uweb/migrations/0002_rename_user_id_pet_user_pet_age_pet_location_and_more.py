# Generated by Django 5.0.1 on 2024-02-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets4uweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='pet',
            name='location',
            field=models.CharField(default='location not specified', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='email_id',
            field=models.EmailField(default='no-email', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='ph_or_email',
            field=models.CharField(default='email', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(default=0),
        ),
    ]
