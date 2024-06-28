
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0006_remove_allkeys_licenseid_allkeys_licenseids_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allkeys',
            name='accountID',
        ),
        migrations.AddField(
            model_name='allkeys',
            name='accountIDS',
            field=models.ManyToManyField(to='ob_app.account'),
        ),
    ]
