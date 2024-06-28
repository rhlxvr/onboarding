
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0017_merge_20220531_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='rolename',
            field=models.CharField(choices=[('Technik', 'Technik'), ('Buchhaltung', 'Buchhaltung'), ('Vertrieb', 'Vertrieb'), ('Marketing', 'Marketing'), ('Einkauf', 'Einkauf'), ('Entwickler', 'Entwickler'), ('Engineer', 'Engineer'), ('-', '-')], max_length=100),
        ),
    ]
