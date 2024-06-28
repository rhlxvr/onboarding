# diese models.py datei definiert die datenbankmodelle für das projekt
# sie wird im django framework verwendet, um datenbanktabellen zu erstellen und zu verwalten
# jedes modell entspricht einer tabelle in der datenbank und gibt die struktur der daten an, die gespeichert werden sollen

from django.db import models
from django.urls import reverse

# modell für neue mitarbeiter
class NewEmployee(models.Model):
    # vererbt von models.Model und repräsentiert neue mitarbeiter in der datenbank
    newEmployeeID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

# modell für bestehende mitarbeiter
class Employee(models.Model):
    # vererbt von models.Model und repräsentiert bestehende mitarbeiter in der datenbank
    employeeID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

# modell für rollen
class Role(models.Model):
    # vererbt von models.Model und repräsentiert rollen, die mitarbeiter haben können
    roleID = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=100)

    def __str__(self):
        return self.rolename

# modell für materialien
class Material(models.Model):
    # vererbt von models.Model und repräsentiert materialien, die einem mitarbeiter zugewiesen werden können
    materialID = models.AutoField(primary_key=True)
    materialname = models.CharField(max_length=50)

    def __str__(self):
        return self.materialname

# modell für lizenzen
class License(models.Model):
    # vererbt von models.Model und repräsentiert lizenzen, die einem mitarbeiter zugewiesen werden können
    licenseID = models.AutoField(primary_key=True)
    licensename = models.CharField(max_length=50)

    def __str__(self):
        return self.licensename

# modell für accounts
class Account(models.Model):
    # vererbt von models.Model und repräsentiert accounts, die einem mitarbeiter zugewiesen werden können
    accountID = models.AutoField(primary_key=True)
    account = models.CharField(max_length=50)

    def __str__(self):
        return self.account

# modell für andere ressourcen
class Other(models.Model):
    # vererbt von models.Model und repräsentiert andere ressourcen, die einem mitarbeiter zugewiesen werden können
    otherID = models.AutoField(primary_key=True)
    other = models.CharField(max_length=50)

    def __str__(self):
        return self.other

# modell für installationen
class Installation(models.Model):
    # vererbt von models.Model und repräsentiert installationen, die einem mitarbeiter zugewiesen werden können
    installationID = models.AutoField(primary_key=True)
    installation = models.CharField(max_length=50)

    def __str__(self):
        return self.installation

# modell für schlüsselsätze
class AllKeys(models.Model):
    # vererbt von models.Model und repräsentiert schlüsselsätze für mitarbeiter
    keyID = models.AutoField(primary_key=True)
    newEmployeeID = models.ForeignKey('NewEmployee', on_delete=models.CASCADE, blank=True, null=True)
    employeeID = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, null=True)
    materialIDS = models.ManyToManyField(Material, blank=True)
    licenseIDS = models.ManyToManyField(License, blank=True)
    accountIDS = models.ManyToManyField(Account, blank=True)
    otherIDS = models.ManyToManyField(Other, blank=True)
    installationIDS = models.ManyToManyField(Installation, blank=True)

    def __str__(self):
        return f"Keys for {self.newEmployeeID}"

    def get_absolute_url(self):
        return reverse('allkeys-details', kwargs={'pk': self.pk})
