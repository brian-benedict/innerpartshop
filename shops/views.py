# # shops/views.py

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Shop  # Import your Shop model
from django.contrib import messages


# @login_required
# def ShopListView(request):
#     # Retrieve the user's associated shop if it exists
#     try:
#         user_shop = request.user.userprofile.shop  # Assuming 'userprofile' is the related name for the UserProfile model
#     except Shop.DoesNotExist:
#         user_shop = None
#         return render(request, 'register_shop.html')


#     # Other view logic here...

#     return render(request, 'shop_list.html', {'user_shop': user_shop})



@login_required
def ShopListView(request):
    # Retrieve the user's associated shop if it exists
    try:
        user_shop = request.user.userprofile.shop  # Assuming 'userprofile' is the related name for the UserProfile model
    except Shop.DoesNotExist:
        user_shop = None

    # Retrieve a list of all shops for the user
    user_shops = Shop.objects.filter(owner=request.user)

    return render(request, 'shop_list.html', {'user_shop': user_shop, 'user_shops': user_shops})

# def register_shop(request):
#     # Your view logic here
#     return render(request, 'register_shop.html')  # Replace with your desired response


def register_shop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        description = request.POST.get('description')

        # Create a new Shop instance and save it to the database
        new_shop = Shop(name=name, owner=request.user, location=location, description=description)
        new_shop.save()

        messages.success(request, 'Shop registered successfully.')
        return redirect('shop-list')  # Replace 'home' with your desired redirect URL

    return render(request, 'register_shop.html')