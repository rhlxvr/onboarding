
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0015_alter_role_rolename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='surname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='newemployee',
            old_name='surname',
            new_name='firstname',
        ),
    ]
