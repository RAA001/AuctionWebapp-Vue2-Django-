from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import Http404
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

# from .forms import OrderForm

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


from .models import Product, Category,Questions,Answers,Profile,Bids
from .serializers import ProductSerializer, CategorySerializer,CreateProductSerializer,CreateQuestionSerializer,CreateAnswerSerializer, GetProfileSerializer,GetBidsSerializer,GetProfileSerializer1,GetImageSerializer

from rest_framework.viewsets import ModelViewSet

from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, SignupForm

from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import generics

from datetime import datetime 
from django.contrib.auth.decorators import login_required

from rest_framework import authentication
from rest_framework import exceptions
from django.urls import reverse_lazy

from django.core.mail import send_mail
from backend import settings

# Create your views here.
User = settings.AUTH_USER_MODEL





"""Fetch all products"""
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


def signup_v(request):
    '''
    Signup function
    Users creating an account
    '''

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']

            password = form.cleaned_data['password']
            # create a new user
            new_user = Profile.objects.create(username=username)
            new_user.email = form.cleaned_data['email']

            # set user's password
            new_user.set_password(password)
            new_user.save()
            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                subject = "Welcome" + username
                message = "Welcome to Technzonezz."
                from_email = settings.EMAIL_HOST_USER
                to_list = [new_user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=False)
                return redirect('product:login')

    return render(request, 'product/signup.html', {'form': SignupForm})

def login_v(request):
    '''
    Login function
    Users logging into the app
    '''

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            print(f"Found user! {user}")
            if user is not None:
                global use1
                use1= user
                auth.login(request, user)
                return redirect('http://localhost:5173/')

            # failed authentication
            return render(request, 'product/login.html', {
                'form': form,
                'error': 'User not registered. Sign up first.'
            })

        # invalid form
        return render(request, 'product/login.html', {
            'form': form
        })

    return render(request, 'product/login.html', {'form': form})

"""Log out function"""
def logout_v(request):
    print(request)
    auth.logout(request)
    use1=None
    return redirect('http://127.0.0.1:8000/')








"""Get all items in the database"""
@api_view(['GET', 'POST'])
def ProductsList(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



"""Create an item in the database"""
@api_view(['GET', 'POST'])
def ProductsList1(request):
    if request.method == 'GET':
        products = Product.objects.filter(user=use1.id)
        serializer = CreateProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('http://localhost:5173/AddProduct')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Class that shows product details"""
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

"""class that shows category details"""
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
"""Search method that allows search for products"""
@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})



"""Fetch and post questions function"""
@api_view(['GET', 'POST'])
def qs(request):
    if request.method == 'GET':
        questions = Questions.objects.all()
        serializer = CreateQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('http://localhost:5173/Questions')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Fetch and post answers function"""
@api_view(['GET', 'POST'])
def answ(request):
    if request.method == 'GET':
        answers = Answers.objects.all()
        serializer = CreateAnswerSerializer(answers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('http://localhost:5173/Answers')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Get Profile of who is logged in and post specific files using this view"""    
@api_view(['GET', 'POST'])
def ProfileList(request):


    if request.method == 'GET':
        request.user=use1
        print(f"Req user: {request.user}")
        profiles = Profile.objects.filter(username=request.user)
        serializer = GetProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.POST, request.FILES)
        id=request.POST.get('user')
        profile=Profile.objects.get(id=int(id))
        profile.image=request.FILES.get('image')
        profile.save()
        return redirect('http://localhost:5173/GImage')
        

    elif request.method == 'PUT':
        profile=Profile.objects.get(id=use1.id)
        serializer = GetProfileSerializer1(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Edit profile function"""
@api_view(['GET', 'PUT', 'DELETE'])
def Profile_detail(request):
    request.user=use1
    try:
        profile = Profile.objects.get(id=use1.id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GetProfileSerializer1(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GetProfileSerializer1(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""View for image"""
@api_view(['GET', 'POST','PUT', 'DELETE'])
def Profileimage(request):
    request.user=use1
    try:
        profile = Profile.objects.get(id=use1.id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GetProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GetProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = GetProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






"""Function that allows getting and posting of bidds"""
@api_view(['GET', 'POST'])
def Bidsview(request):
    if request.method == 'GET':
        bids = Bids.objects.order_by('-product','-price')
        serializer = GetBidsSerializer(bids, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GetBidsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('http://localhost:5173/Bids')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Function that fetches all of the emails within the database"""
@api_view(['GET'])
def Emailpage(request):
    if request.method == 'GET':
        emails = Profile.objects.all()
        serializer = GetProfileSerializer(emails, many=True)
        return Response(serializer.data)