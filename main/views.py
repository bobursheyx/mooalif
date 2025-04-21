# views.py
from django.shortcuts import render, redirect
from .forms import ArizaForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ArizaForm(request.POST)
        if form.is_valid():
            form.save()  # Ariza ma'lumotlarini saqlash
            messages.success(request, 'Arizangiz muvaffaqiyatli yuborildi.')
            return redirect('home')  # Yuborilgandan keyin home sahifasiga qaytish
    else:
        form = ArizaForm()

    return render(request, 'home.html', {'form': form})
