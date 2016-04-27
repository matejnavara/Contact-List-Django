from django.shortcuts import render
from django.db.models import Q
from .models import Employee
import re

def employee_list(request):
    """ Default view displays the active employees and orders them based on last name.
    """
    employees = Employee.objects.filter(is_active=True).order_by('last_name')
    return render(request, 'employee_list.html', {'employees' : employees})

def sort(request):
    """ Orders the table based on the column selected.
    """
    order = request.GET.get('order_by','')
    employees = Employee.objects.all().filter(is_active=True).order_by(order)
    return render(request, 'employee_list.html', {'employees' : employees})

def search(request):
    """ Searches fields for query string and displays the found entries from:
        first name, last name, email, address, city, post code and telephone //currently doesnt like the ForeignKey fields.
    """
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query = request.GET['q']
        entry_query = get_query(query, ['first_name', 'last_name', 'email', 'address', 'city', 'post_code','telephone',])
        found_entries = Employee.objects.filter(entry_query).filter(is_active=True)
    return render(request, 'employee_list.html', {'employees': found_entries})
                      



def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """ Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.    
    """
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    """ Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.  
    """
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
