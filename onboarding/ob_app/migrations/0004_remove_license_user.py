
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0003_remove_allkeys_materialid_allkeys_materialids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='user',
        ),
    ]
