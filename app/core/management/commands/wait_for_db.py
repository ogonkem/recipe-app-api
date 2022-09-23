"""
Django comand to wait for the database to be available
"""
from email.policy import default
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait fot database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up == False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!'))
