from django.shortcuts import render, redirect
from phonebook.models import PhoneBook
# Create your views here.
def test(request):
   # print("GET userId : "+request.GET.get('userId'))
    #print("GET userPw : "+request.GET.get('userPw'))

#    print("GET userId : "+request.POST.get('userId'))
#    print("GET userPw : "+request.POST.get('userPw'))
    return render(request,"PBook/test.html")

def index(request):
    alluser = PhoneBook.objects.values('id', '이름','전화번호')
    
    context = {"PhoneBook":alluser}
    print(alluser)
    return render(request,"PBook/index.html",context)

def add(request):
        if request.method == 'POST':
            print("name : "+request.POST.get('name'))
            print("phNum : "+request.POST.get('phNum'))
            print("email : "+request.POST.get('email'))
            print("addr : "+request.POST.get('addr'))
            print("bir : "+request.POST.get('bir'))
            
            table = PhoneBook()
            table.이름 = request.POST.get('name')
            table.전화번호 = request.POST.get('phNum')
            table.이메일 = request.POST.get('email')
            table.주소 = request.POST.get('addr')
            table.생년월일 = request.POST.get('bir')
            table.save()
            
            return redirect('PB:index')
        else:
            return render(request,"PBook/add.html")

def delete(request):
    return render(request,"PBook/delete.html")

def detail(request,userId):
    userInfo = PhoneBook.objects.values('id', '이름','전화번호','주소','이메일','생년월일').get(id=userId)
    
    print(userInfo)
    context = {"PhoneBook":userInfo}
    return render(request,"PBook/detail.html",context)

def update(request,updateId):
    table = PhoneBook.objects.get(id=updateId)
    
    context = {"phonebook":table}
    return render(request,"PBook/update.html",context)