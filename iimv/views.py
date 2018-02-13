from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
import csv

def index(request):
	return render(request,'index.html',{})

def achievements(request):
	pass

def aboutus(request):
	return render(request,'about.html',{})

def contactus(request):
	contactusdata = ContactUs.objects.all()
	context = {'contact' : contactusdata}		
	return render(request,'contact.html',context)

def events(request):
	eventsdata = Event.objects.all().order_by('-date')
	context = {'events':eventsdata}
	return render(request,'events.html',context)

def executivecouncil(request):
	list_council = ExecutiveMembers.objects.all().order_by('srn')
	return render(request,'member.html',{'list':list_council})

def photogallery(request):
	pass					

def sendmsg(request):
	data = request.POST
	send_mail(
    'IIM Query',
    data['message'],
    data['email'],
    ['hpaliwal4@gmail.com'],
    fail_silently=True,
	)
	return redirect('/contactus')

def memberlist(request):
	return render(request,'members.html',{})


def memberlistdown(request,cat):
	if cat == 'Total':
		cat = ''
	name = 'MEMBERS_' + cat + '.csv'
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=' + name
	writer = csv.writer(response)
	rows = []
	with open('iimv/csv_members_list/varanasipaid.csv','r') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			if row[1].find(cat) != -1 or row[1] == 'CATCODE':
				rows.append(row)			

	for row in rows:
		writer.writerow(row)

	return response				