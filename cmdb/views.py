from django.shortcuts import render
# Create your views here.
from cmdb import models
from cmdb.bookworm import static_historyworm_main



def historyhtml(request):

    static_historyworm_main()
    book_list=models.bookInfo.objects.all()
    return render(request, "booktop.html", {"data":book_list})