from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateAcount, Login, Manager
from .models import Person
from django.contrib import messages
# Create your views here.



class CurrnetPeople():
	name = ""
	phone = ""
	email = ""

	def setDetails(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return self.name + " " + self.phone + " " + self.email

currnetPeople = CurrnetPeople()

def signup(response):
	if response.method == "POST":
		persons = Person.objects.all()
		names = []
		for p in persons:
			names.append(p.name)
		
		if response.POST["name"] not in names:
			detailedForm = Person(name=response.POST["name"], phone=response.POST["phone"], email=response.POST["email"]) 
			p1 = Person(name=detailedForm.name, phone=detailedForm.phone, email=detailedForm.email)
			p1.save()
			print("User Added !")

	form = CreateAcount()
	return render(response, "main/signup.html", {"form":form})



def login(response):
	if response.method == "POST":
		try:
			phone = Person.objects.get(name = response.POST["name"]).phone
			if phone == response.POST["phone"]:
				print("sucssess")
				currnetPeople.setDetails(Person.objects.get(name = response.POST["name"]).name, Person.objects.get(name = response.POST["name"]).phone, Person.objects.get(name = response.POST["name"]).email)
				return HttpResponseRedirect('/myprofile')
			else:
				print("unsucssess")
		except:
			print("user name is not in database")


	form = Login()
	return render(response, "main/login.html", {"form": form})

def myprofile(response):
	print(currnetPeople)
	return render(response, "main/myprofile.html", {"currnetPeople": currnetPeople})

def home(response):
	return render(response, "main/home.html", {})

def manager(response):
	if response.method == "POST":
		if response.POST["name"] == "sagi" and response.POST["password"] == "sagi":
			return HttpResponseRedirect("/users")
	form = Manager()
	return render(response, "main/manager.html", {"form": form})

def users(response):
	users = Person.objects.all()
	return render(response, "main/users.html", {"users": users})
