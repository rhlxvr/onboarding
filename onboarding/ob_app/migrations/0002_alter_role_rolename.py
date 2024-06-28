
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='rolename',
            field=models.CharField(choices=[('Technik', 'Technik'), ('Buchhaltung', 'Buchhaltung'), ('Vertrieb', 'Vertrieb'), ('Marketing', 'Marketing'), ('Einkauf', 'Einkauf'), ('Entwickler', 'Entwickler')], max_length=100),
        ),
    ]
