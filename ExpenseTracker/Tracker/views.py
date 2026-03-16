from django.shortcuts import render, redirect
from .models import Expense, Income
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')

    return render(request, 'login.html')


# REGISTER
def registration(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('login')

    return render(request, 'reg.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# HOME
@login_required
def Home(request):

    expenses = Expense.objects.filter(user=request.user)
    income = Income.objects.filter(user=request.user)

    total_expense = sum(exp.amount for exp in expenses)
    total_income = sum(inc.amount for inc in income)

    balance = total_income - total_expense

    context = {
        'expenses': expenses,
        'income': income,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance
    }

    return render(request, 'home.html', context)


# ADD EXPENSE
@login_required
def add_expense(request):

    if request.method == "POST":

        title = request.POST.get('title')
        amount = float(request.POST.get('amount'))
        category = request.POST.get('category')
        date = request.POST.get('date')

        expense = Expense(
            user=request.user,
            title=title,
            amount=amount,
            category=category,
            date=date
        )

        expense.save()

        return redirect('Home')

    return render(request, 'expense.html')


# ADD INCOME
@login_required
def add_income(request):

    if request.method == "POST":

        source = request.POST.get('source')
        amount = request.POST.get('amount')
        date = request.POST.get('date')

        income = Income(
            user=request.user,
            source=source,
            amount=amount,
            date=date
        )

        income.save()

        return redirect('Home')

    return render(request, 'income.html')


# DISPLAY EXPENSES
@login_required
def expense_display(request):

    expenses = Expense.objects.filter(user=request.user)

    return render(request, 'expense_display.html', {'expenses': expenses})


# DELETE EXPENSE
@login_required
def delete_expense(request, id):

    expense = Expense.objects.get(pk=id, user=request.user)

    expense.delete()

    return redirect('Home')