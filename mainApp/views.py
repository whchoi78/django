from django.shortcuts import render

def test(request ,name):
    print(name,"접속했습니다.")
    return render(request, "myhtml/test.html")