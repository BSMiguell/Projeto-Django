from django.shortcuts import render

# Create your views here.

# ===== HOME PAGE =====
def home (request):
    return render(request, 'index.html')

# ===== TIMELINE PAGE =====
def timeline (request):
    return render(request, 'timeline.html')

# ===== ABOUT =====
def about (request):
    return render(request, 'about.html')

# ===== ABOUT-DETALHES =====
def aboutDetalhes1 (request):
    return render(request, 'detalhes-about-1.html')
def aboutDetalhes2 (request):
    return render(request, 'detalhes-about-2.html')
def aboutDetalhes3 (request):
    return render(request, 'detalhes-about-3.html')

# ===== ABOUT-US =====
def aboutUs (request):
    return render(request, 'about-Us.html')

# ===== PRODUCTS SUB-PAGES ===== 
def products1 (request):
    return render(request, 'products1.html')
def products2 (request):
    return render(request, 'products2.html')
def products3 (request):
    return render(request, 'products3.html')

# =====  PARE SUB-PAGE ===== 
def pare (request):
    return render(request, 'pare.html')

# =====  COMMON-QUESTIONS SUB-PAGE ===== 
def common (request):
    return render(request, 'common-questions.html')

# =====  DETALHES SUB-PAGE ===== 
def detalhes (request):
    return render(request, 'detalhes.html')

# =====  PRICING SUB-PAGE ===== 
def pricing (request):
    return render(request, 'pricing.html')

# =====  LOGIN SUB-PAGE ===== 
def login (request):
    return render(request, 'login.html')

# =====  user-index ===== 
def userIndex (request):
    return render(request, 'user-index.html')