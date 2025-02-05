
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from django.shortcuts import get_object_or_404

class ProductAPI(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddToCartAPI(APIView):
    def post(self, request, format=None):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        product = get_object_or_404(Product, id=product_id)

        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CartAPI(APIView):
    def get(self, request, format=None):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = request.user
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        cart_item = get_object_or_404(CartItem, user=user, product=product)
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
















# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from .serializers import ProductSerializer
# from .models import Product

# # from django.http import JsonResponse
# from .service import Cart

# class ProductAPI(APIView):
#     #  API to handle product operations
    
#     serializer_class = ProductSerializer

#     def get(self, request, format=None):
#         qs = Product.objects.all()

#         return Response(
#             {"data": self.serializer_class(qs, many=True).data}, 
#             status=status.HTTP_200_OK
#             )

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             serializer.data, 
#             status=status.HTTP_201_CREATED
#             )
    
# class CartAPI(APIView):
    
#     # Single API to handle cart operations
    
#     def get(self, request, format=None):
#         cart = Cart(request)
#         return Response(
#             {"data": list(cart.__iter__()), 
#              "cart_total_price": cart.get_total_price()},
#             status=status.HTTP_200_OK
#         )

#     def post(self, request, **kwargs):
#         cart = Cart(request)
#         data = request.data

#         if "remove" in data:
#             product_id = data.get("product")
#             if not product_id:
#                 return Response({"error": "Product ID is required for removal."},
#                                 status=status.HTTP_400_BAD_REQUEST)
#             cart.remove(product_id)

#         elif "clear" in data:
#             cart.clear()

#         else:
#             product_id = data.get("product")
#             quantity = data.get("quantity")
#             # override_quantity = data.get("override_quantity", False)

#             if not product_id or quantity is None:
#                 return Response(
#                     {"error": "Product ID and quantity are required to add/update cart."},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )

#             cart.add(
#                 product=product_id,
#                 quantity=quantity
#                 # override_quantity=override_quantity
#             )

#         return Response(
#             {"message": "cart updated"},
#             status=status.HTTP_202_ACCEPTED
#         )
    





















# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Cart, CartItem, Product
# from .serializers import CartSerializer, CartItemSerializer

# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Ensure users can only see their own cart
#         return Cart.objects.filter(user=self.request.user)

#     def create(self, request, *args, **kwargs):
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity', 1)

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         if not created:
#             cart_item.quantity += int(quantity)
#             cart_item.save()

#         serializer = self.get_serializer(cart)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         cart = self.get_object()
#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity', 1)

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cart_item.quantity = int(quantity)
#         cart_item.save()

#         serializer = self.get_serializer(cart)
#         return Response(serializer.data, status=status.HTTP_200_OK)



















# from django.shortcuts import render
# from django.shortcuts import render, redirect
# from .models import Product, CartItem
# from rest_framework import response
# from rest_framework.views import APIView


# class carview(APIView):

#     def get(request):
# 	    products = Product.objects.all()

# 	    return response()

#     def view_cart(request):
# 	    cart_items = CartItem.objects.filter(user=request.user)
# 	    total_price = sum(item.product.price * item.quantity for item in cart_items)
# 	    return response()

# def add_to_cart(request, product_id):
# 	product = Product.objects.get(id=product_id)
# 	cart_item, created = CartItem.objects.get_or_create(product=product, 
# 													user=request.user)
# 	cart_item.quantity += 1
# 	cart_item.save()
# 	return redirect('cart:view_cart')

# def remove_from_cart(request, item_id):
# 	cart_item = CartItem.objects.get(id=item_id)
# 	cart_item.delete()
# 	return redirect('cart:view_cart')




