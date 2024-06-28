# Onboarding Application

Dieses Projekt ist eine Onboarding-Anwendung, die mit dem Django-Framework entwickelt wurde. Die Anwendung verwaltet neue und bestehende Mitarbeiter sowie verschiedene Ressourcen wie Materialien, Lizenzen, Accounts, Rollen und Installationen.

## Konzept

Die Anwendung basiert auf einem objektorientierten Ansatz und umfasst die folgenden Hauptkomponenten:
- **NewEmployee**: Modell zur Verwaltung neuer Mitarbeiter.
- **Employee**: Modell zur Verwaltung bestehender Mitarbeiter.
- **Role**: Modell zur Verwaltung von Mitarbeiterrollen.
- **Material**: Modell zur Verwaltung von Materialien.
- **License**: Modell zur Verwaltung von Lizenzen.
- **Account**: Modell zur Verwaltung von Accounts.
- **Other**: Modell zur Verwaltung anderer Ressourcen.
- **Installation**: Modell zur Verwaltung von Installationen.
- **AllKeys**: Modell zur Verknüpfung von Mitarbeitern mit verschiedenen Ressourcen.

## Anforderungen

- Django Framework
- Python 3.x
- Virtuelle Umgebung (empfohlen)

## Installation

1. Aktivieren Sie die bestehende virtuelle Umgebung:
    ```bash
    source myenv/bin/activate
    ```

2. Installieren Sie die Abhängigkeiten aus der `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Datenbankmigrationen

1. Erstellen Sie die Datenbankmigrationen:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Admin-Account

Ein Admin-Account wurde erstellt, um auf das Admin-Interface und auf die Anwendung zuzugreifen:
- **Benutzername**: macromedia
- **Passwort**: macromedia

## Django-Server starten

1. Starten Sie den Django-Entwicklungsserver:
    ```bash
    python3 manage.py runserver
    ```

2. Greifen Sie auf die Anwendung im Browser zu:
    ```
    http://127.0.0.1:8000/
    ```

## Nutzung der Anwendung

Nach dem Starten des Servers können Sie auf die verschiedenen Funktionen der Anwendung zugreifen, darunter:
- Hinzufügen, Anzeigen, Aktualisieren und Löschen von Mitarbeitern und Ressourcen.
- Verwaltung der Mitarbeiterrollen, Materialien, Lizenzen, Accounts, Installationen und anderer Ressourcen.

Die Anwendung enthält verschiedene Ansichten und URLs für jede dieser Funktionen. Die Zugriffsrechte werden basierend auf der Benutzerrolle verwaltet.

## Weitere Informationen

Für weitere Details zur Implementierung und den genauen Funktionsumfang der Anwendung, siehe die Dokumentation und Kommentare im Code.
