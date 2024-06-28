
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0012_rename_installations_installation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='provided',
        ),
        migrations.RemoveField(
            model_name='installation',
            name='provided',
        ),
        migrations.RemoveField(
            model_name='license',
            name='provided',
        ),
        migrations.RemoveField(
            model_name='material',
            name='provided',
        ),
        migrations.RemoveField(
            model_name='other',
            name='provided',
        ),
        migrations.RemoveField(
            model_name='role',
            name='provided',
        ),
    ]
