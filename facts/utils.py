import requests
from .models import Fact

def fetch_and_save_facts(num_facts=500):
    """Fetches a specified number of facts and saves them to the database."""
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    saved_facts = 0
    for _ in range(num_facts):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            fact_text = data.get("text")
            if fact_text:
                Fact.objects.get_or_create(text=fact_text)
                saved_facts += 1
        except requests.exceptions.RequestException as e:
            print(f"Error fetching fact: {e}")
            continue
    return saved_facts