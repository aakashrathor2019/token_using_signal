from django.apps import AppConfig

class SignalAppConfig(AppConfig):
    name = "signal_app"

    def ready(self):
        import signal_app.signals  # Ensure signals are imported
