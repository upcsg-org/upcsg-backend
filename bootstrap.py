#!/usr/bin/env python

import os
import subprocess
import sys

def install_dependencies():
    """Install the required Python packages."""
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def set_environment_variables():
    """Set up environment variables required for Django."""
    print("Setting environment variables...")
    os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
    os.environ['PYTHONPATH'] = os.getcwd()

def run_migrations():
    """Run database migrations."""
    print("Running migrations...")
    subprocess.check_call([sys.executable, 'manage.py', 'migrate'])

def collect_static_files():
    """Collect static files."""
    print("Collecting static files...")
    subprocess.check_call([sys.executable, 'manage.py', 'collectstatic', '--noinput'])

def create_superuser():
    """Optionally, create a superuser."""
    print("Creating superuser...")
    subprocess.check_call([sys.executable, 'manage.py', 'createsuperuser'])

def main():
    install_dependencies()
    set_environment_variables()
    run_migrations()
    collect_static_files()
    
    # Uncomment the following line if you want to create a superuser automatically
    # create_superuser()

    print("Django project setup complete. You can now run the server with:")
    print("python manage.py runserver")

if __name__ == "__main__":
    main()
