import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "production_api.settings")


from django.core.management import execute_from_command_line
import sys

if __name__ == "__main__":
    # Execute Django commands
    execute_from_command_line(sys.argv)
