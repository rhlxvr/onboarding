# Generated by Django 4.0.3 on 2022-04-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountID', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=50)),
                ('provided', models.BooleanField(default=False, verbose_name='account')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('materialID', models.AutoField(primary_key=True, serialize=False)),
                ('materialname', models.CharField(max_length=50)),
                ('provided', models.BooleanField(default=False, verbose_name='material')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('roleID', models.AutoField(primary_key=True, serialize=False)),
                ('rolename', models.CharField(choices=[('Technician', 'Technik'), ('Accounting', 'Buchhaltung'), ('Sales', 'Vertrieb'), ('Marketing', 'Marketing'), ('CommercialPurchases', 'Einkauf'), ('Developer', 'Entwickler')], max_length=100)),
                ('provided', models.BooleanField(default=False, verbose_name='role')),
            ],
        ),
        migrations.CreateModel(
            name='NewEmployee',
            fields=[
                ('newEmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.role')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('licenseID', models.AutoField(primary_key=True, serialize=False)),
                ('licensename', models.CharField(choices=[('WIN', 'Windows'), ('OFF', 'Office')], max_length=3)),
                ('provided', models.BooleanField(default=False, verbose_name='license')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.newemployee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.role')),
            ],
        ),
        migrations.CreateModel(
            name='AllKeys',
            fields=[
                ('keyID', models.AutoField(primary_key=True, serialize=False)),
                ('accountID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.account')),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.employee')),
                ('licenseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.license')),
                ('materialID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.material')),
                ('newEmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ob_app.newemployee')),
            ],
        ),
    ]
