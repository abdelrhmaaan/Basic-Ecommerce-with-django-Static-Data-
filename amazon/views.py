from django.shortcuts import render


# Create your views here.

# def hello_world(request):
#     return HttpResponse('Hello,Word')

# def bootstrap(request):
#     return HttpResponse(' <h1 style="color : red "> Hello Word</h1>'  )

# def hiFriend(request,friend):
#     return HttpResponse(f'Hi {friend}')

# def home_page(request):
#     return render(request,'amazon/index.html')

# dict 
products = [
    {"name": "Product 1", "price": 19.99,'id':1,'img':"images/pic1.jpg"},
    {"name": "Product 2", "price": 29.99,'id':2,'img':"images/pic2.jpg" },
    {"name": "Product 3", "price": 9.99,'id':3 ,'img':"images/pic3.jpg"}
]

def return_to_homepage(request):
    return render(request, 'amazon/index.html',context={'products': products})

def about_us(request):
    return render(request,'amazon/aboutus.html')

def contact_us(request):
    return render(request,'amazon/contact.html')

def product_page(request,id):
    product = products[ id -1 ]
    return render(request,'amazon/productpage.html',{'product':product})