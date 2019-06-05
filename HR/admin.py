from django.contrib import admin
from HR.models import Post,Entrepreneur_content,Student_content,QA
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     list_display=('username',
#                 'first_name',
#                 'last_name',
#                 'password',
#                 'email',
#                 'phone',
#                 'addredd',
#                 'groups',
#                 'is_staff',
#                 'is_active',
#                 'last_login',
#                 'date_joined')



class PostAdmin(admin.ModelAdmin):
    list_display = ('postid',
                    'entrepreneur',
                    'jobtype',
                    'title',
                    'detail',
                    'condition',
                    'contact',
                    'benefit',
                    'min_salary',
                    'post_date',
                    'viewed',
                    'like')


class Entrepreneur_contentAdmin(admin.ModelAdmin):
    list_display = ('entrepreneur','introduction','address','phone')


class Student_contentAdmin(admin.ModelAdmin):
    list_display = ('student','mis_id','resume')


class QAAdmin(admin.ModelAdmin):
    list_display = ('qaid','student','entrepreneur','post','content','post_date')

admin.site.register(QA,QAAdmin)
admin.site.register(Student_content,Student_contentAdmin)
admin.site.register(Entrepreneur_content,Entrepreneur_contentAdmin)
admin.site.register(Post,PostAdmin)
# admin.site.register(User,CustomUserAdmin)

# ------------old line
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('ArticleId',
#     'VendorId',
#     'AContent_title',
#     'Type',
#     'MinSalary',
#     'AContent_detail',
#     'Acontent_condition',
#     'AContent_benefit',
#     'AContent_contact',
#     'Views',
#     'Like',
#     'PostingTime')

# class VendorAdmin(admin.ModelAdmin):
#     list_display = ('VendorId','Name','Password','Email','Phone','Address')

# class QAAdmin(admin.ModelAdmin):
#     list_display = ('QAId','ArticleId','ClientId','VendorId','QContent','PostingTime')

# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('ClientId','Name','Password','Email','Phone','Resume')


# admin.site.register(Post,PostAdmin)
# admin.site.register(Vendor,VendorAdmin)
# admin.site.register(QA,QAAdmin)
# admin.site.register(Client,ClientAdmin)
