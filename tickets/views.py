from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_tickets(request):
    # Logic to retrieve tickets for the logged-in user
    tickets = request.user.created_tickets.all()  # Assuming you want to show tickets created by the user
    return render(request, 'tickets/my_tickets.html', {'tickets': tickets})