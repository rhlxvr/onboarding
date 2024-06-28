
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0009_merge_20220428_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='provided',
            field=models.BooleanField(default=False, verbose_name='license'),
        ),
    ]
