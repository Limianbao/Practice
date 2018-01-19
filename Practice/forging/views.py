#coding:utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from forms import UserForm
from .models import User
# Create your views here.
def first(request):
	uname=request.session.get('name','未登录')

	return render(request,'forging/first_bloor.html',{'uname':uname})

def deletes(request):  #删除session里储存的用户信息（姓名）
	del request.session['name']
	return render(request, 'forging/first_bloor.html')





def registered(request):   #registered=注册
	if request.method == 'POST':
		user = UserForm(request.POST,request.FILES)
		#print (request.POST.get('sex'))
		print (1111111111111111111111111111111111111111111111111)
		if user.is_valid():
			print (22222222222222222222222222222222222222222222222)
			# img=User(head_portrait=request.FILES.get('head_portrait'))
			# img.save()
			user.save()

			print (3333333333333333333333333333333333333333333333)
			request.session['name']=request.POST['name']	#设置注册成功后自动加入session缓存
			#两种重导向分别需要导入的模块
				#from django.shortcuts import render,redirect
				#from django.core.urlresolvers import reverse
				#from django.http import HttpResponseRedirect
			print(444444444444444444444444444444444444444444444444)
			return redirect(reverse('forging:success'))
			#return HttpResponseRedirect(reverse('forging:success'))
		else :
			return HttpResponse('注册失败')
	else:
		user=UserForm()
	return render(request,'forging/registered.html',{'user':user})


def landing(request):   #landing=登录
	pass


def query(request):   #query=查询
	pass


def success(request):  #注册成功后跳转的成功网页
	return render(request,'forging/success.html')
