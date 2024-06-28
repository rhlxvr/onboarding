
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob_app', '0007_remove_allkeys_accountid_allkeys_accountids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('otherID', models.AutoField(primary_key=True, serialize=False)),
                ('other', models.CharField(max_length=50)),
                ('provided', models.BooleanField(default=False, verbose_name='other')),
            ],
        ),
        migrations.AddField(
            model_name='allkeys',
            name='otherIDS',
            field=models.ManyToManyField(to='ob_app.other'),
        ),
    ]
