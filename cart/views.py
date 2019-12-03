from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    pledge = int(request.POST.get('pledge'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, pledge)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    pledge = int(request.POST.get('pledge'))
    cart = request.session.get('cart', {})

    if pledge > 0:
        cart[id] = pledge
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))