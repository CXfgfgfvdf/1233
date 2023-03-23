# Generated by Django 3.2.18 on 2023-03-21 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0066_alter_cloudstorage_credentials_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientfile',
            options={'default_permissions': (), 'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='relatedfile',
            options={'default_permissions': (), 'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='remotefile',
            options={'default_permissions': (), 'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='serverfile',
            options={'default_permissions': (), 'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='remotefile',
            unique_together={('data', 'file')},
        ),
        migrations.AlterUniqueTogether(
            name='serverfile',
            unique_together={('data', 'file')},
        ),
    ]
