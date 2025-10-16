from django.core.management.base import BaseCommand
from facts.utils import fetch_and_save_facts

class Command(BaseCommand):
    help = 'Fetches facts from an external API and populates the database.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching facts and populating the database...")
        num_saved = fetch_and_save_facts(num_facts=500)
        self.stdout.write(self.style.SUCCESS(f"Successfully saved {num_saved} facts."))
