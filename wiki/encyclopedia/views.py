from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(entry_content)
    })

def search(request):
    query = request.GET.get('q')
    if query:
        entries = util.list_entries()
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
        if len(matching_entries) == 1 and query.lower() == matching_entries[0].lower():
            return redirect(reverse('entry', args=[matching_entries[0]]))
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": matching_entries
        })
    return redirect(reverse('index'))

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new_page.html", {
                "error": "An entry with this title already exists."
            })
        util.save_entry(title, content)
        return redirect(reverse("entry", args=[title]))
    return render(request, "encyclopedia/new_page.html")

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect(reverse("entry", args=[title]))
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": entry_content
    })

def random_page(request):
    entries = util.list_entries()
    if entries:
        random_title = random.choice(entries)
        return redirect(reverse("entry", args=[random_title]))
    return redirect(reverse("index"))