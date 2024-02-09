# Generated by Django 5.0.1 on 2024-02-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets4uweb', '0002_rename_user_id_pet_user_pet_age_pet_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_id',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ph_or_email',
            field=models.CharField(default='Email', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
