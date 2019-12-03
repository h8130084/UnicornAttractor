from django.shortcuts import get_object_or_404
from tickets.models import Bug

def cart_content(request):
    
# keeps pledges avilable when rendering any page

    cart = request.session.get('cart', {})
    
    cart_items = []
    total= 0
    bug_count = 0

    for id, pledge in cart.items():
        bug = get_object_or_404(Bug, pk=id)
        
        total += pledge
        bug_count += 1
        cart_items.append({'id': id, 'pledge': pledge, 'bug': bug})
    
    return {'cart_items': cart_items, 'total': total, 'bug_count': bug_count}