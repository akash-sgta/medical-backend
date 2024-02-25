# ========================================================================
import os
import sys
from datetime import datetime

# ========================================================================


def post_error_to_terminal(text: str):
    now = datetime.now()
    current_date = f"{now.year}-{now.month}-{now.day}"
    current_time = now.strftime("%H:%M:%S")
    print(f"[X] [{current_date} {current_time}] {text}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    else:
        execute_from_command_line(sys.argv)
        try:
            execute_from_command_line(sys.argv)
        except Exception as e:
            post_error_to_terminal(str(e))
            raise KeyboardInterrupt


if __name__ == "__main__":
    main()
