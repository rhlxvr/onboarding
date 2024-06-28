
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0011_installations_allkeys_installationdis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Installations',
            new_name='Installation',
        ),
    ]
