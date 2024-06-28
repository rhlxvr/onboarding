
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0010_license_provided'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installations',
            fields=[
                ('installationID', models.AutoField(primary_key=True, serialize=False)),
                ('installation', models.CharField(max_length=50)),
                ('provided', models.BooleanField(default=False, verbose_name='other')),
            ],
        ),
        migrations.AddField(
            model_name='allkeys',
            name='installationDIS',
            field=models.ManyToManyField(to='ob_app.installations'),
        ),
    ]
