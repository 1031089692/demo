# Generated by Django 2.0.5 on 2018-12-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_actionapi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionapi',
            name='created_by',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='actionapi',
            name='descriptions',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='actionapi',
            name='updated_by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]