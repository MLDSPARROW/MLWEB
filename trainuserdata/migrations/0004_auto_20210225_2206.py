# Generated by Django 3.1.7 on 2021-02-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainuserdata', '0003_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('dataset_code', models.CharField(blank=True, max_length=100, null=True)),
                ('dataset', models.FileField(upload_to='datasets/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
