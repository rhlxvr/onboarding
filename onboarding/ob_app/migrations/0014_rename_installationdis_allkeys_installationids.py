
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0013_remove_account_provided_remove_installation_provided_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allkeys',
            old_name='installationDIS',
            new_name='installationIDS',
        ),
    ]
