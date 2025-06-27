from django.shortcuts import render
from .forms import Eventform,AttendeeForm,TicketForm
from .models import Event,Attendee,Ticket
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def event_form(request):
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'event_form.html', {'events': events})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = Eventform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_form')  # Redirect to event list after creating
    else:
        form = Eventform()

    return render(request, 'create_event.html', {'form': form})
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = Eventform(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_form')  
    else:
        form = Eventform(instance=event)

    return render(request, 'edit_event.html', {'form': form})
@login_required
def delete_event(request,event_id):
    event=get_object_or_404(Event,pk=event_id)
    if request.method=="POST":
        event.delete()
        return redirect('event_form')
    return render(request,'delete_event.html',{'event':event})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Attendee
from .forms import AttendeeForm
@login_required
def register_attend(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('event_form')  
    else:
        form = AttendeeForm()
    
    return render(request, 'register_attend.html', {'form': form})

@login_required
def ticket_system(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event
            ticket.save()
            return redirect('view_ticket', ticket_id=ticket.id)  
    else:
        form = TicketForm()

    return render(request, 'ticket_system.html', {'form': form, 'event': event})


def details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = Ticket.objects.filter(event=event)
    total_revenue = sum(ticket.price for ticket in tickets)
    total_attendees = len(set(ticket.attendee.id for ticket in tickets))
    return render(request, 'details.html', {
        'event': event,
        'tickets': tickets,
        'total_revenue': total_revenue,
        'total_attendees': total_attendees,
    })
@login_required
def edit_ticket(request,ticket_id):
    ticket=get_object_or_404(Ticket,pk=ticket_id)
    if request.method=="POST":
     form=TicketForm(request.POST,request.FILES,instance=ticket)
     if form.is_valid():
         form.save()
         return redirect('details', event_id=ticket.event.id)
    else:
        form=TicketForm(instance=ticket)
    return render(request,'edit_ticket.html',{'form': form,'ticket':ticket})
@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    event_id = ticket.event.id if ticket.event else None
    if request.method == 'POST':
        ticket.delete()
        return redirect('details', event_id=event_id)
    return render(request, 'delete_ticket.html', {'ticket': ticket, 'event_id': event_id})
from django.shortcuts import render
from .models import Ticket

def all_attendees(request):
    tickets = Ticket.objects.select_related('event', 'attendee').all()
    return render(request, 'all_attendees.html', {'tickets': tickets})

from django.shortcuts import render
from .models import Ticket

def event_tickets(request):
    tickets = Ticket.objects.select_related('event', 'attendee').all()
    total_revenue = sum(t.price for t in tickets)
    confirmed = tickets.filter(status='a').count()
    pending = tickets.filter(status='b').count()
    cancelled = tickets.filter(status='c').count()

    return render(request, 'event_tickets.html', {
        'tickets': tickets,
        'total_revenue': total_revenue,
        'confirmed': confirmed,
        'pending': pending,
        'cancelled': cancelled,
    })
from django.db.models import Q
def search_results(request):
    query = request.GET.get('q')
    events = Event.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    attendees = Attendee.objects.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )
    tickets = Ticket.objects.filter(
        Q(seat_number__icontains=query) | Q(status__icontains=query)
    )

    return render(request, 'search_results.html', {
        'query': query,
        'events': events,
        'attendees': attendees,
        'tickets': tickets
    })

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'view_ticket.html', {'ticket': ticket})

def download_ticket_pdf(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    template = get_template('view_ticket.html')
    html = template.render({'ticket': ticket})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{ticket.id}.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    return response if not pisa_status.err else HttpResponse('PDF error')