from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from todo.models import TodoModel
from django.contrib import messages
from datetime import datetime
from django.db.models import Q


# Create your views here.

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            user_works = TodoModel.objects.filter(user=request.user).order_by("-id")
            query = request.GET.get('query')

            if query:
                user_works = TodoModel.objects.filter(Q(name__contains = query))

            context = {
                "user_works": user_works
            }
            return render(request, 'index.html', context)
        else:  
            return render(request, 'index.html')
        
    
    def post(self, request, *args, **kwargs):
        # choice = request.POST.get("choice")

        # if choice=="create":
        work = request.POST.get("work")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        print(type(start_time))
        print(type(end_time))
        # end_time = "salam"
        # work = "salam"
        # if not work:
        #     work = "salam"
        if request.user.is_authenticated:    
            if work and start_time:
                user_work  = TodoModel.objects.create(
                name = work,
                start_time = start_time,
                end_time = end_time or None,
                user = request.user
            )
                
            if not work:
                messages.info(request, "enter work name please")
            if not start_time:
                messages.info(request, "enter start time please")
                

        return redirect("todo:index")
        
        # elif choice=="update":
        #     id = request.POST.get("id")
        #     user_work = TodoModel.objects.get(id=id)
        #     name = request.POST.get("work")
        

        #     user_work.name = name
        #     user_work.save()

            # return redirect("todo:index")
    


def update_work(request, id):
    user_work = TodoModel.objects.get(id=id)
    print(user_work)

    if request.method == "POST":
        name = request.POST.get("work")
        if not name:
            messages.info(request, "enter work name please")
            return render(request, "work_update.html")
        else:
            user_work.name = name
            user_work.save()
            return redirect('todo:index')
    return render(request, 'work_update.html')


def update_start_time(request, id):
    user_work = TodoModel.objects.get(id=id)
    print(user_work)

    if request.method == "POST":
        start_time = request.POST.get("time")
        print(start_time)
        if not start_time:
            messages.info(request, "enter time please")
            return redirect('todo:start_time_update', id =id)
        else:
            print(user_work.start_time)
            # user_work.start_time = False
            user_work.start_time = start_time
            #class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
            user_work.save()
            return redirect('todo:index')
        
    return render(request, 'start_time_update.html')            


def update_end_time(request, id):
    user_work = TodoModel.objects.get(id=id)

    if request.method == "POST":
        end_time = request.POST.get('time')
        if not end_time:
            messages.info(request,"enter time please")
            return redirect('todo:end_time_update', id=id)
        else:
            user_work.end_time = end_time
            user_work.save()
            return redirect("todo:index")
    return render(request, 'end_time_update.html')

    



def delete_(request, id):
    user_work =TodoModel.objects.get(id=id)
    # print(user_work)
    user_work.delete()
    # TodoModel.objects.get(id=id).delete()
    return redirect('todo:index')    



