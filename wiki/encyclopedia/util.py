import re
import os

from django.conf import settings

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    for _, _, filenames in os.walk(os.path.join(settings.BASE_DIR, "entries")):
        return list(sorted(filename[:-3] for filename in filenames if filename.endswith(".md")))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filepath = os.path.join(settings.BASE_DIR, "entries", f"{title}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        with open(os.path.join(settings.BASE_DIR, "entries", f"{title}.md"), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None