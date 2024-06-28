
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0005_remove_license_provided_alter_allkeys_materialids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allkeys',
            name='licenseID',
        ),
        migrations.AddField(
            model_name='allkeys',
            name='licenseIDS',
            field=models.ManyToManyField(to='ob_app.License'),
        ),
        migrations.AddField(
            model_name='license',
            name='provided',
            field=models.BooleanField(default=False, verbose_name='license'),
        ),
        migrations.AlterField(
            model_name='license',
            name='licensename',
            field=models.CharField(max_length=50),
        ),
    ]
