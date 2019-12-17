from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """ generates the carts content page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a feature alongside its pledge to the cart"""
    
    pledge = int(request.POST.get('pledge'))
    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] = cart[id] + pledge
    else:
        cart[id] = cart.get(id, pledge)

    request.session['cart'] = cart
    return redirect(reverse('bug'))


def adjust_cart(request, id):
    """Adjust the pledge of the  feature"""
    pledge = int(request.POST.get('pledge'))
    cart = request.session.get('cart', {})

    if pledge > 0:
        cart[id] = pledge
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))