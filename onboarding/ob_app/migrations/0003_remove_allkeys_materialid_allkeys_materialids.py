
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0002_alter_role_rolename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allkeys',
            name='materialID',
        ),
        migrations.AddField(
            model_name='allkeys',
            name='materialIDS',
            field=models.ManyToManyField(to='ob_app.material'),
        ),
    ]
