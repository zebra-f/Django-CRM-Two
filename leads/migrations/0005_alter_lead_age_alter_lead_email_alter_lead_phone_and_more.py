# Generated by Django 4.0.5 on 2022-07-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_lead_email_lead_phone_alter_lead_age_leadstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='leadstatus',
            name='private_note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='leadstatus',
            name='public_note',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
