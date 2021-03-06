from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from models import Books, Issuebook, usergroups

def IsAdminUser(user):
    return user.is_staff

@login_required
def dasboard(request):
    global group_name
    user = request.user
    if request.method == "GET":
        if not user.is_staff:
            try:
                if usergroups.objects.get(username=user.username):
                    return render(request, "lend/home.html", {'has_group': True})
            except:
                return render(request, "lend/home.html", {'has_group': False})
        else:
            return render(request, "lend/home.html")
    elif request.method == "POST":
        gp_name = request.POST['filter']
        try:
            g = usergroups.objects.get(username=user.username)
            group_name = g.group
        except:
            user_group = usergroups(username=user.username, group=gp_name)
            group_name = gp_name
            user_group.save()
        group = Group.objects.get(name=gp_name)
        group.user_set.add(request.user)
        print user.groups.filter(name=gp_name).exists()
        return render(request, "lend/home.html", {'has_group': True})

@login_required
@user_passes_test(IsAdminUser)
def addbook(request):
    books = Books.objects.all()
    if request.user.is_staff:
        if request.method == "POST":
            name = request.POST['book']
            author = request.POST['author']
            copies = request.POST['copies']
            status = request.POST['status']
            book = Books(name=name, author=author, copies=copies, status=status)
            book.save()
            return redirect("/lend/addbook")
        else:
            return render(request, "lend/addbook.html", {'books': books})

def lend(request):
    if request.method == "POST":
        if group_name=="students":
            return studentissue(request)
        else:
            return teacherissue(request)
    else:
        books = Books.objects.all()
        issuedetails = Issuebook.objects.filter(username=request.user.username)
        return render(request, "lend/lendbook.html", {'books': books, 'history': issuedetails})

def studentissue(request):
    book = request.POST['bookname']
    books = Books.objects.all()
    u = request.user
    status = getbookstatus(request, book)
    if status:
        try:
            issuedetails = Issuebook.objects.filter(username=u).reverse()[0]
            if issuedetails.can_issue:
                issuedetails.issued += 1
                issuedetails.can_issue -= 1
                status = True
                issuedetails.save()
            else:
                status = False
            return render(request, "lend/lendbook.html", {'books': books, 'status': status, 'history': issuedetails})
        except:
            issuedetails = Issuebook(username=u, bookname=book, groupname="students", issued=1, can_issue=2)
            issuedetails.save()
            issuedetails = Issuebook.objects.filter(username=u)
            return render(request, "lend/lendbook.html", {'books': books, 'status': True, 'history': issuedetails})
    else:
        return render(request, "lend/lendbook.html", {'books': books, 'status': False})

def teacherissue(request):
    book = request.POST['bookname']
    books = Books.objects.all()
    u = request.user
    status = getbookstatus(request, book)
    if status:
        try:
            issuedetails = Issuebook.objects.filter(username=u).reverse()[0]
            print issuedetails, issuedetails.can_issue
            if issuedetails.can_issue:
                issuedetails.issued += 1
                issuedetails.can_issue -= 1
                status = True
                issuedetails.save()
            else:
                status = False
            return render(request, "lend/lendbook.html", {'books': books, 'status': status, 'history': issuedetails})
        except:
            issuedetails = Issuebook(username=u, bookname=book, groupname="teachers", issued=1, can_issue=5)
            issuedetails.save()
            issuedetails = Issuebook.objects.filter(username=u)
            #print issuedetails
            return render(request, "lend/lendbook.html", {'books': books, 'status': True, 'history': issuedetails})
    else:
        return render(request, "lend/lendbook.html", {'books': books, 'status': False})

def getbookstatus(request, book):
    print book
    bookdetails = Books.objects.get(name=book)
    print bookdetails.status
    if bookdetails.status:
        bookdetails.copies -= 1
        if bookdetails.copies == 0:
            bookdetails.status = False
        bookdetails.save()
        return True
    else:
        return False

def details(request):
    u = request.user
    users = Issuebook.objects.all()
    books = Books.objects.all()
    return render(request, "lend/details.html", {'users': users, 'books':books, 'user':u})