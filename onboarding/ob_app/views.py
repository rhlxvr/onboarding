# diese views.py datei definiert die ansichten für das projekt
# sie wird im django framework verwendet, um die logik für verschiedene webseiten und funktionen zu erstellen
# jede ansicht entspricht einer seite oder funktionalität auf der webseite und enthält die logik, die ausgeführt wird, wenn ein nutzer die seite aufruft

# importiere notwendige module und funktionen von django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

# importiere die modelle, die in models.py definiert sind
from .models import License, Employee, NewEmployee, Material, AllKeys, Account, Role, Other, Installation

# importiere klassen für generische ansichten von django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importiere module für benutzerauthentifizierung und zugriffssteuerung
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import AllKeysForm, NewEmployeeForm


# mixin, um zu prüfen, ob der nutzer ein admin ist
class UserIsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# mixin, um zu prüfen, ob der nutzer eingeloggt ist
class UserIsAuthenticatedMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated


# einfache ansicht, die eine "hello world" nachricht zurückgibt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# ansicht für die startseite, nur zugänglich für eingeloggte nutzer
@login_required(login_url='/login')
def home(request):
    return render(request, 'ob_app/home.html')


# ansicht für eine zusätzliche seite
def extras(request):
    return render(request, 'ob_app/extras.html')


# ansicht zum ausloggen des nutzers
def logout_user(request):
    logout(request)
    return render(request, 'ob_app/logout.html')


### materials ###
# ansichten für die verwaltung von materialien
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von materialien

# ansicht zum erstellen eines neuen materials, nur für admins
class MaterialCreateView(UserIsAdminMixin, CreateView):
    model = Material
    fields = ['materialID', 'materialname']
    template_name = 'ob_app/materials/create.html'
    context_object_name = 'materials'
    success_url = reverse_lazy('materials-list')


# ansicht zum anzeigen der liste aller materialien, nur für eingeloggte nutzer
class MaterialListView(UserIsAuthenticatedMixin, ListView):
    model = Material
    template_name = 'ob_app/materials/list.html'
    context_object_name = 'materials'


# ansicht zum anzeigen der details eines materials, nur für admins
class MaterialDetailView(UserIsAdminMixin, DetailView):
    model = Material
    template_name = 'ob_app/materials/details.html'


# ansicht zum aktualisieren eines materials, nur für admins
class MaterialUpdateView(UserIsAdminMixin, UpdateView):
    model = Material
    fields = ['materialID', 'materialname']
    template_name = 'ob_app/generell/update.html'


# ansicht zum löschen eines materials, nur für admins
class MaterialDeleteView(UserIsAdminMixin, DeleteView):
    model = Material
    fields = ['materialID', 'materialname']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('materials-list')


### accounts ###
# ansichten für die verwaltung von accounts
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von accounts

# ansicht zum erstellen eines neuen accounts, nur für admins
class AccountCreateView(UserIsAdminMixin, CreateView):
    model = Account
    fields = ['accountID', 'account']
    template_name = 'ob_app/accounts/create.html'
    context_object_name = 'accounts'
    success_url = reverse_lazy('accounts-list')


# ansicht zum anzeigen der liste aller accounts, nur für eingeloggte nutzer
class AccountListView(UserIsAuthenticatedMixin, ListView):
    model = Account
    template_name = 'ob_app/accounts/list.html'
    context_object_name = 'accounts'


# ansicht zum anzeigen der details eines accounts, nur für admins
class AccountDetailView(UserIsAdminMixin, DetailView):
    model = Account
    template_name = 'ob_app/accounts/details.html'


# ansicht zum aktualisieren eines accounts, nur für admins
class AccountUpdateView(UserIsAdminMixin, UpdateView):
    model = Account
    fields = ['accountID', 'account']
    template_name = 'ob_app/generell/update.html'


# ansicht zum löschen eines accounts, nur für admins
class AccountDeleteView(UserIsAdminMixin, DeleteView):
    model = Account
    fields = ['accountID', 'account']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('accounts-list')


### licenses ###
# ansichten für die verwaltung von lizenzen
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von lizenzen

# ansicht zum erstellen einer neuen lizenz, nur für admins
class LicenseCreateView(UserIsAdminMixin, CreateView):
    model = License
    fields = ['licenseID', 'licensename']
    template_name = 'ob_app/licenses/create.html'
    context_object_name = 'licenses'
    success_url = reverse_lazy('licenses-list')


# ansicht zum anzeigen der liste aller lizenzen, nur für eingeloggte nutzer
class LicenseListView(UserIsAuthenticatedMixin, ListView):
    model = License
    template_name = 'ob_app/licenses/list.html'
    context_object_name = 'licenses'


# ansicht zum anzeigen der details einer lizenz, nur für admins
class LicenseDetailView(UserIsAdminMixin, DetailView):
    model = License
    template_name = 'ob_app/licenses/details.html'


# ansicht zum aktualisieren einer lizenz, nur für admins
class LicenseUpdateView(UserIsAdminMixin, UpdateView):
    model = License
    fields = ['licenseID', 'licensename']
    template_name = 'ob_app/generell/update.html'


# ansicht zum löschen einer lizenz, nur für admins
class LicenseDeleteView(UserIsAdminMixin, DeleteView):
    model = License
    fields = ['licenseID', 'licensename']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('licenses-list')


### roles ###
# ansichten für die verwaltung von rollen
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von rollen

# ansicht zum erstellen einer neuen rolle, nur für admins
class RoleCreateView(UserIsAdminMixin, CreateView):
    model = Role
    fields = ['roleID', 'rolename']
    template_name = 'ob_app/roles/create.html'
    context_object_name = 'roles'
    success_url = reverse_lazy('roles-list')


# ansicht zum anzeigen der liste aller rollen, nur für eingeloggte nutzer
class RoleListView(UserIsAuthenticatedMixin, ListView):
    model = Role
    template_name = 'ob_app/roles/list.html'
    context_object_name = 'roles'


# ansicht zum anzeigen der details einer rolle, nur für admins
class RoleDetailView(UserIsAdminMixin, DetailView):
    model = Role
    template_name = 'ob_app/roles/details.html'


# ansicht zum aktualisieren einer rolle, nur für admins
class RoleUpdateView(UserIsAdminMixin, UpdateView):
    model = Role
    fields = ['roleID', 'rolename']
    template_name = 'ob_app/generell/update.html'


# ansicht zum löschen einer rolle, nur für admins
class RoleDeleteView(UserIsAdminMixin, DeleteView):
    model = Role
    fields = ['roleID', 'rolename']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('roles-list')


### installations ###
# ansichten für die verwaltung von installationen
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von installationen

# ansicht zum erstellen einer neuen installation, nur für admins
class InstallationCreateView(UserIsAdminMixin, CreateView):
    model = Installation
    fields = ['installationID', 'installation']
    template_name = 'ob_app/installations/create.html'
    context_object_name = 'installations'
    success_url = reverse_lazy('installations-list')


# ansicht zum anzeigen der liste aller installationen, nur für eingeloggte nutzer
class InstallationListView(UserIsAuthenticatedMixin, ListView):
    model = Installation
    template_name = 'ob_app/installations/list.html'
    context_object_name = 'installations'


# ansicht zum anzeigen der details einer installation, nur für admins
class InstallationDetailView(UserIsAdminMixin, DetailView):
    model = Installation
    template_name = 'ob_app/installations/details.html'


# ansicht zum aktualisieren einer installation, nur für admins
class InstallationUpdateView(UserIsAdminMixin, UpdateView):
    model = Installation
    fields = ['installationID', 'installation']
    template_name = 'ob_app/generell/update.html'


# ansicht zum löschen einer installation, nur für admins
class InstallationDeleteView(UserIsAdminMixin, DeleteView):
    model = Installation
    fields = ['installationsID', 'installation']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('installations-list')


### others ###
# ansichten für die verwaltung von anderen ressourcen
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von anderen ressourcen

# ansicht zum erstellen einer neuen anderen ressourcen, nur für admins
class OtherCreateView(UserIsAdminMixin, CreateView):
    model = Other
    fields = ['otherID', 'other']
    template_name = 'ob_app/others/create.html'
    context_object_name = 'others'
    success_url = reverse_lazy('others-list')


# ansicht zum anzeigen der liste aller anderen ressourcen, nur für eingeloggte nutzer
class OtherListView(UserIsAuthenticatedMixin, ListView):
    model = Other
    template_name = 'ob_app/others/list.html'
    context_object_name = 'others'


# ansicht zum anzeigen der details einer anderen ressourcen, nur für admins
class OtherDetailView(UserIsAdminMixin, DetailView):
    model = Other
    template_name = 'ob_app/others/details.html'


# ansicht zum aktualisieren einer anderen ressourcen, nur für admins
class OtherUpdateView(UserIsAdminMixin, UpdateView):
    model = Other
    fields = ['otherID', 'other']
    template_name = 'ob_app/generell/update.html'


# ansicht zum löschen einer anderen ressourcen, nur für admins
class OtherDeleteView(UserIsAdminMixin, DeleteView):
    model = Other
    fields = ['otherID', 'othername']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('others-list')


### allkeys ###
# ansichten für die verwaltung von schlüsselsätzen
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von schlüsselsätzen

# ansicht zum anzeigen der liste aller schlüsselsätze, nur für eingeloggte nutzer
class AKListView(UserIsAuthenticatedMixin, ListView):
    model = AllKeys
    template_name = 'ob_app/onboarding/list.html'


# ansicht zum anzeigen der liste aller schlüsselsätze, nur für eingeloggte nutzer
class KeysListView(UserIsAuthenticatedMixin, ListView):
    model = AllKeys
    template_name = 'ob_app/test2.html'
    context_object_name = 'keys'


# ansicht zum erstellen eines neuen schlüsselsatzes, nur für eingeloggte nutzer
class AKCreateView(CreateView):
    model = AllKeys
    form_class = AllKeysForm
    template_name = 'ob_app/onboarding/create.html'
    success_url = '/allkeys/'  # oder eine andere URL Ihrer Wahl


# ansicht zum aktualisieren eines schlüsselsatzes, nur für eingeloggte nutzer
class AKUpdateView(UpdateView):
    model = AllKeys
    form_class = AllKeysForm
    template_name = 'ob_app/onboarding/update.html'
    success_url = '/allkeys/'  # oder eine andere URL Ihrer Wahl


# ansicht zum löschen eines schlüsselsatzes, nur für eingeloggte nutzer
class AKDeleteView(UserIsAuthenticatedMixin, DeleteView):
    model = AllKeys
    fields = ['newEmployeeID', 'employeeID', 'materialIDS', 'licenseIDS', 'accountIDS', 'otherIDS']
    template_name = "ob_app/onboarding/delete.html"
    success_url = reverse_lazy('allkeys-list')


# ansicht zum anzeigen der details eines schlüsselsatzes, nur für eingeloggte nutzer
class AllKeysDetailView(UserIsAuthenticatedMixin, DetailView):
    model = AllKeys
    template_name = "ob_app/onboarding/details.html"


### newemployee ###
# ansichten für die verwaltung von neuen mitarbeitern
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von neuen mitarbeitern

# ansicht zum erstellen eines neuen mitarbeiters, nur für eingeloggte nutzer
class NewEmployeeCreateView(CreateView):
    model = NewEmployee
    form_class = NewEmployeeForm
    template_name = 'ob_app/new-employees/create.html'
    success_url = '/onboarding/create'


# ansicht zum anzeigen der liste aller neuen mitarbeiter, nur für eingeloggte nutzer
class NewEmployeeListView(UserIsAuthenticatedMixin, ListView):
    model = NewEmployee
    template_name = 'ob_app/new-employees/list.html'
    context_object_name = 'newEmployee'


# ansicht zum anzeigen der details eines neuen mitarbeiters, nur für eingeloggte nutzer
class NewEmployeeDetailView(UserIsAuthenticatedMixin, DetailView):
    model = NewEmployee
    template_name = "ob_app/new-employees/details.html"


# ansicht zum aktualisieren eines neuen mitarbeiters, nur für eingeloggte nutzer
class NewEmployeeUpdateView(UserIsAuthenticatedMixin, UpdateView):
    model = NewEmployee
    fields = ['firstname', 'lastname', 'role']
    template_name = 'ob_app/generell/update.html'
    success_url = reverse_lazy('newemployee-list')


# ansicht zum löschen eines neuen mitarbeiters, nur für admins
class NewEmployeeDeleteView(UserIsAdminMixin, DeleteView):
    model = NewEmployee
    fields = ['firstname', 'lastname', 'role']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('newemployee-list')


### employee ###
# ansichten für die verwaltung von bestehenden mitarbeitern
# diese ansichten umfassen das erstellen, anzeigen, aktualisieren und löschen von bestehenden mitarbeitern

# ansicht zum erstellen eines neuen mitarbeiters, nur für eingeloggte nutzer
class EmployeeCreateView(UserIsAuthenticatedMixin, CreateView):
    model = Employee
    fields = ['firstname', 'lastname', 'role']
    template_name = 'ob_app/employees/create.html'
    context_object_name = 'Employee'
    success_url = reverse_lazy('onboarding-start')


# ansicht zum anzeigen der liste aller mitarbeiter, nur für eingeloggte nutzer
class EmployeeListView(UserIsAuthenticatedMixin, ListView):
    model = Employee
    template_name = 'ob_app/employees/list.html'
    context_object_name = 'Employee'


# ansicht zum anzeigen der details eines mitarbeiters, nur für eingeloggte nutzer
class EmployeeDetailView(UserIsAuthenticatedMixin, DetailView):
    model = Employee
    template_name = "ob_app/employees/details.html"


# ansicht zum aktualisieren eines mitarbeiters, nur für eingeloggte nutzer
class EmployeeUpdateView(UserIsAuthenticatedMixin, UpdateView):
    model = Employee
    fields = ['firstname', 'lastname', 'role']
    template_name = 'ob_app/generell/update.html'
    success_url = reverse_lazy('employee-list')


# ansicht zum löschen eines mitarbeiters, nur für admins
class EmployeeDeleteView(UserIsAdminMixin, DeleteView):
    model = Employee
    fields = ['firstname', 'lastname', 'role']
    template_name = 'ob_app/generell/delete.html'
    success_url = reverse_lazy('employee-list')
