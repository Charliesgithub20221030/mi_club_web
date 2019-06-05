from django.db import models
from django.conf import settings


class Student_content(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True)
    resume = models.TextField()
    mis_id = models.CharField( max_length=10)

    def __str__(self):
        return self.student.username

class Entrepreneur_content(models.Model):
    entrepreneur = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE,
                                primary_key=True)
    introduction = models.TextField()
    address = models.CharField( max_length=200)
    phone = models.CharField( max_length=50)

    def __str__(self):
        return self.entrepreneur.username

class Post(models.Model):
    postid = models.IntegerField(primary_key=True)
    entrepreneur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jobtype = models.CharField( max_length=50)
    title = models.CharField( max_length=100)
    detail = models.TextField()
    condition = models.TextField()
    benefit = models.TextField()
    contact = models.TextField()
    min_salary = models.PositiveIntegerField()
    viewed = models.IntegerField()
    like = models.IntegerField()
    post_date = models.DateTimeField( auto_now=True)


    def __str__(self):
        return self.title


class QA(models.Model):
    qaid = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student_content, on_delete=models.CASCADE)
    entrepreneur = models.ForeignKey(Entrepreneur_content, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField( auto_now=True)


    def __str__(self):
        return self.post





##---------------------old line--------------------
# class Vendor(models.Model):
#     VendorId =models.IntegerField(primary_key=True)
#     Name = models.CharField( max_length=50)
#     Password = models.CharField( max_length=50)
#     Email = models.EmailField( max_length=254)
#     Phone = models.IntegerField()
#     Address = models.CharField( max_length=255)

#     def __str__(self):
#         return self.Name

# class Post(models.Model):
#     ArticleId = models.IntegerField(primary_key=True)
#     VendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     Type = models.CharField( max_length=50)
#     AContent_title=models.CharField(max_length=50)
#     AContent_detail = models.TextField()
#     Acontent_condition=models.TextField()
#     AContent_benefit=models.TextField()
#     AContent_contact=models.TextField()
#     Views = models.IntegerField()
#     Like = models.IntegerField()
#     PostingTime = models.DateTimeField( auto_now=True, auto_now_add=False)
#     MinSalary = models.IntegerField()
#     def __str__(self):
#         return self.AContent
# class Client(models.Model):
#     ClientId = models.IntegerField(primary_key=True)
#     Name = models.CharField( max_length=50)
#     Password = models.CharField( max_length=50)
#     Email = models.EmailField( max_length=254)
#     Phone = models.IntegerField()
#     Resume = models.TextField()

#     def __str__(self):
#         return self.Name

# class QA(models.Model):
#     QAId = models.IntegerField(primary_key=True)
#     ArticleId = models.ForeignKey(Post, on_delete=models.CASCADE)
#     ClientId = models.ForeignKey(Client, on_delete=models.CASCADE)
#     VendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     QContent = models.TextField()
#     PostingTime = models.DateTimeField( auto_now=True, auto_now_add=False)

#     def __str__(self):
#         return self.QContent


# # class Administrator(models.Model):
# #     Ad = models.IntegerField(pimary_key=True)
# #     Password = models.CharField( max_length=50)
# #     Name = models.CharField( max_length=50)

# #     def __str__(self):
# #         return self.Name

