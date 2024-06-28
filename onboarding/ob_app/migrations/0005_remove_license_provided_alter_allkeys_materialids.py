
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0004_remove_license_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='provided',
        ),
        migrations.AlterField(
            model_name='allkeys',
            name='materialIDS',
            field=models.ManyToManyField(to='ob_app.Material'),
        ),
    ]
