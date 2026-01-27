from django.shortcuts import render


def index(request):
    """
    Simple landing page view.
    """
    return render(request, "index.html")


def create_rule(request):
    """
    Page explaining how to create project rules.
    """
    return render(request, "create_rule.html")
