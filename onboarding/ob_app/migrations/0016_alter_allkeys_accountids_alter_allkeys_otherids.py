
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0015_alter_role_rolename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allkeys',
            name='accountIDS',
            field=models.ManyToManyField(to='ob_app.Account'),
        ),
        migrations.AlterField(
            model_name='allkeys',
            name='otherIDS',
            field=models.ManyToManyField(to='ob_app.Other'),
        ),
    ]
