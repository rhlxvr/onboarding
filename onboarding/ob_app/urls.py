# diese urls.py datei definiert die URL-routen für das projekt
# sie wird im django framework verwendet, um URLs mit ansichten zu verknüpfen
# jede route entspricht einer URL und gibt an, welche ansicht aufgerufen wird, wenn die URL aufgerufen wird

# importiere die path funktion, um URL-muster zu definieren
from django.urls import path

# importiere die ansichten (views) aus der views.py datei
# diese ansichten enthalten die logik, die ausgeführt wird, wenn eine URL aufgerufen wird
from .views import AKCreateView, AllKeysDetailView, AKDeleteView, AKUpdateView, \
    AKListView, NewEmployeeCreateView, NewEmployeeListView, NewEmployeeDetailView, NewEmployeeUpdateView, \
    NewEmployeeDeleteView, EmployeeDeleteView, EmployeeListView, EmployeeDetailView, EmployeeUpdateView, \
    EmployeeCreateView, \
    MaterialCreateView, MaterialUpdateView, MaterialDeleteView, MaterialDetailView, MaterialListView, \
    AccountCreateView, AccountListView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    LicenseListView, LicenseCreateView, LicenseDeleteView, LicenseDetailView, LicenseUpdateView, \
    RoleListView, RoleCreateView, RoleDeleteView, RoleDetailView, RoleUpdateView, OtherListView, OtherCreateView, \
    OtherDetailView, OtherUpdateView, OtherDeleteView, InstallationListView, InstallationCreateView, \
    InstallationDeleteView, InstallationDetailView, InstallationUpdateView

# importiere die ansichten von django für die benutzer-authentifizierung (login und logout)
from django.contrib.auth import views as auth_views

# importiere die eigenen ansichten aus der views.py datei
from . import views

urlpatterns = [
    # allgemeine seiten wie home, extras, login und logout
    # diese urls sind für generelle seiten der webseite
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('extras/', views.extras, name='extras'),
    path('login/', auth_views.LoginView.as_view(template_name="ob_app/login.html"), name='login'),
    path('logout/', views.logout_user, name='logout'),

    # urls für die verwaltung von schlüsselsätzen (AllKeys)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von schlüsselsätzen befassen
    path('onboarding/create', AKCreateView.as_view(), name='onboarding-start'),
    path('allkeys/<int:pk>', AllKeysDetailView.as_view(), name='allkeys-details'),
    path('allkeys/<int:pk>/update', AKUpdateView.as_view(), name='allkeys-update'),
    path('allkeys/<int:pk>/delete', AKDeleteView.as_view(), name='allkeys-delete'),
    path('allkeys/', AKListView.as_view(), name='allkeys-list'),

    # urls für die verwaltung von neuen mitarbeitern (NewEmployee)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von neuen mitarbeitern befassen
    path('newemployee/create', NewEmployeeCreateView.as_view(), name='newemployee-create'),
    path('newemployee/list', NewEmployeeListView.as_view(), name='newemployee-list'),
    path('newemployee/<int:pk>', NewEmployeeDetailView.as_view(), name='newemployee-details'),
    path('newemployee/<int:pk>/update', NewEmployeeUpdateView.as_view(), name='newemployee-update'),
    path('newemployee/<int:pk>/delete', NewEmployeeDeleteView.as_view(), name='newemployee-delete'),
    path('newemployee-create', NewEmployeeCreateView.as_view(), name='newemployee-create'),

    # urls für die verwaltung von bestehenden mitarbeitern (Employee)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von bestehenden mitarbeitern befassen
    path('employee/create', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/list', EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee-details'),
    path('employee/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee-delete'),

    # urls für die verwaltung von materialien (Material)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von materialien befassen
    path('materials/list', MaterialListView.as_view(), name='materials-list'),
    path('materials/create', MaterialCreateView.as_view(), name='materials-create'),
    path('material/<int:pk>', MaterialDetailView.as_view(), name='materials-details'),
    path('material/<int:pk>/update', MaterialUpdateView.as_view(), name='materials-update'),
    path('material/<int:pk>/delete', MaterialDeleteView.as_view(), name='materials-delete'),

    # urls für die verwaltung von lizenzen (License)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von lizenzen befassen
    path('licenses/list', LicenseListView.as_view(), name='licenses-list'),
    path('licenses/create', LicenseCreateView.as_view(), name='licenses-create'),
    path('licenses/<int:pk>', LicenseDetailView.as_view(), name='licenses-details'),
    path('licenses/<int:pk>/update', LicenseUpdateView.as_view(), name='licenses-update'),
    path('licenses/<int:pk>/delete', LicenseDeleteView.as_view(), name='licenses-delete'),

    # urls für die verwaltung von accounts (Account)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von accounts befassen
    path('accounts/list', AccountListView.as_view(), name='accounts-list'),
    path('accounts/create', AccountCreateView.as_view(), name='accounts-create'),
    path('accounts/<int:pk>', AccountDetailView.as_view(), name='accounts-details'),
    path('accounts/<int:pk>/update', AccountUpdateView.as_view(), name='accounts-update'),
    path('accounts/<int:pk>/delete', AccountDeleteView.as_view(), name='accounts-delete'),

    # urls für die verwaltung von rollen (Role)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von rollen befassen
    path('roles/list', RoleListView.as_view(), name='roles-list'),
    path('roles/create', RoleCreateView.as_view(), name='roles-create'),
    path('roles/<int:pk>', RoleDetailView.as_view(), name='roles-details'),
    path('roles/<int:pk>/update', RoleUpdateView.as_view(), name='roles-update'),
    path('roles/<int:pk>/delete', RoleDeleteView.as_view(), name='roles-delete'),

    # urls für die verwaltung von anderen ressourcen (Other)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von anderen ressourcen befassen
    path('others/list', OtherListView.as_view(), name='others-list'),
    path('others/create', OtherCreateView.as_view(), name='others-create'),
    path('others/<int:pk>', OtherDetailView.as_view(), name='others-details'),
    path('others/<int:pk>/update', OtherUpdateView.as_view(), name='others-update'),
    path('others/<int:pk>/delete', OtherDeleteView.as_view(), name='others-delete'),

    # urls für die verwaltung von installationen (Installation)
    # diese urls sind für seiten, die sich mit der erstellung, anzeige, aktualisierung und löschung von installationen befassen
    path('installations/list', InstallationListView.as_view(), name='installations-list'),
    path('installations/create', InstallationCreateView.as_view(), name='installations-create'),
    path('installations/<int:pk>', InstallationDetailView.as_view(), name='installations-details'),
    path('installations/<int:pk>/update', InstallationUpdateView.as_view(), name='installations-update'),
    path('installations/<int:pk>/delete', InstallationDeleteView.as_view(), name='installations-delete'),
]
