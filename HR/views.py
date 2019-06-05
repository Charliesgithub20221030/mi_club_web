from django.shortcuts import render,render_to_response,get_object_or_404
from HR.models import Post
from django.contrib.auth.decorators import permission_required

# useful function
def is_member(user,group):
    return user.groups.filter(name=group.name).exists()

# view function
def index(request):
    return render_to_response('index.html')

# test permission required decorator
@permission_required('HR.can_post')
def about(request):
    return render_to_response('about.html')

def job(request):
    post_list=Post.objects.all()
    return render(request,'job.html',{'posts':post_list})
def job_view(request,jid):
    job_data=get_object_or_404(Post,Id=jid)
    # job_data=Post.objects.get(ArticleId=jid)
    return render(request,'job_view.html',
    {'title':job_data.AContent_title,
    'type':job_data.Type,
    'detail':job_data.AContent_detail,
    'condition':job_data.Acontent_condition,
    'benefit':job_data.AContent_benefit,
    'contact':job_data.AContent_contact,
    'postTime':job_data.PostingTime})


def member_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        


    return render_to_response('member_login.html')

def member_signup(request): #name studentId email pwd
    pass
#     公司介紹
# 產業類別：
# 電腦軟體服務業
# 產業描述：
# 資訊服務業
# 員　　工：
# 暫不提供
# 資 本 額：
# 10億
# 聯 絡 人：
# 總管理處
# 公司地址：
# 台北市中正區杭州南路一段26號8樓地圖
# 電　　話：
# 暫不提供
# 傳　　真：
# 暫不提供
# 公司網址：
# https://www.chtsecurity.com
# 相關連結：
# 更多
def company_signup(request): #name industry phone address email asset pwd

    pass
def company_signup_action(request):
    pass

def member_login_action(request):
    return render(reqest,'index.html')

def member_signup(request):
    pass

def member_signup_action(request):
    pass

def company_login(request):
    return render_to_response('company_login.html')
    
def company_login_action(request):
    return render(reqest,'index.html')