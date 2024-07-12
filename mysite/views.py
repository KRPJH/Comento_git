from django.shortcuts import render
from .models import MainContent

# Create your views here.
def index(request):

    content_list = MainContent.objects.order_by('-pub_date') #질문목록 출력 / (-)기호로 역순(최신순)
    context={'content_list':content_list}
    return render(request, 'mysite/content_list.html', context) #content_list데이터를 파일에 적용후 HTML 리턴
