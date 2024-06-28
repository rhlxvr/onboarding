
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0004_remove_license_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='provided',
        ),
    ]
