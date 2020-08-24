from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
from random import randint
import fnmatch
import csv

categories =[]
questions = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
names = ["","",""]
money = [0,0,0]
show1 = False
show2 = False
show3 = False

with open(f"entries/JeopardyTest2.csv") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			categories = row
			line_count += 1
		else:
			n = 0
			for item in row: 
				print(item)
				questions[n].append(item)
				n += 1
			line_count += 1
	print(categories)
class NewEntryForm(forms.Form):
	Player1 = forms.CharField(label="Player1")
	Player2 = forms.CharField(label="Player2")
	Player3 = forms.CharField(label="Player3")

class MoneyForm(forms.Form):
	pass
#	def __init__(self,*args,**kwargs):
#		player = kwargs.pop('Player')
#		super(StylesForm,self).__init__(*args,**kwargs)
    
class DailyDoubleForm(forms.Form):
	Body = forms.CharField(widget=forms.Textarea, label="Body")
    
def home(request):

        	# If not, create a new list
	request.session["show1"] = False
	request.session["show2"] = False
	request.session["show3"] = False

	if request.method == "POST" :
		form = NewEntryForm(request.POST)
		if form.is_valid():
			names[0] = form.cleaned_data["Player1"]
			names[1] = form.cleaned_data["Player2"]
			names[2] = form.cleaned_data["Player3"]
			return render(request, "jeopardy/single.html", {
				"categories": categories[0:6],
				"questions": questions[0:6],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
	return render(request, "jeopardy/index.html", {
	    "form": NewEntryForm()
	})
    
def single(request):

	if request.method == "POST":
		if request.POST.get("correct") == "Correct":
			print(request.POST.get("valueH"))
			money[int(request.POST.get("player"))] += int(request.POST.get("valueH"))
			return render(request, "jeopardy/single.html", {
				"categories": categories[0:6],
				"questions": questions[0:6],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
		if request.POST.get("correct") == "Incorrect":
			print(request.POST.get("valueH"))
			money[int(request.POST.get("player"))] -= int(request.POST.get("valueH"))
			return render(request, "jeopardy/single.html", {
				"categories": categories[0:6],
				"questions": questions[0:6],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
	return render(request, "jeopardy/single.html", {
		"categories": categories[0:6],
		"questions": questions[0:6],
		"p1": names[0],
		"dollal1": money[0],
		"p2": names[1],
		"dollal2": money[1],
		"p3": names[2],
		"dollal3": money[2]
	}) 
	
def double(request):

	if request.method == "POST":
		if request.POST.get("correct") == "Correct":
			print(request.POST.get("valueH"))
			money[int(request.POST.get("player"))] += int(request.POST.get("valueH"))
			return render(request, "jeopardy/double.html", {
				"categories": categories[6:12],
				"questions": questions[6:12],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
		if request.POST.get("correct") == "Incorrect":
			print(request.POST.get("valueH"))
			money[int(request.POST.get("player"))] -= int(request.POST.get("valueH"))
			return render(request, "jeopardy/double.html", {
				"categories": categories[6:12],
				"questions": questions[6:12],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
	return render(request, "jeopardy/double.html", {
		"categories": categories[6:12],
		"questions": questions[6:12],
		"p1": names[0],
		"dollal1": money[0],
		"p2": names[1],
		"dollal2": money[1],
		"p3": names[2],
		"dollal3": money[2]
	}) 
        
def question2(request, catnum, qnum):
	if((catnum==3 and qnum==3) or (catnum==2 and qnum==4)):
		return render(request, "jeopardy/dailyd.html", {
				"catnum": catnum+6,
				"qnum": qnum,
	       		"text": questions[int(catnum)+6][int(qnum)],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
	value =400*(int(qnum)+1)
	if request.method == "POST":
		if request.POST.get("correct") == "Correct":
			money[int(request.POST.get("player"))] += value
			return render(request, "jeopardy/double.html", {
				"categories": categories[6:12],
				"questions": questions[0:6],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
		money[int(request.POST.get("player"))] -= int(request.POST.get("valueH"))
		return render(request, "jeopardy/question2.html", {
			"catnum": catnum,
			"qnum": qnum,
       		"text": questions[int(catnum)+6][int(qnum)],
			"valueP": value,
			"p1": names[0],
			"dollal1": money[0],
			"p2": names[1],
			"dollal2": money[1],
			"p3": names[2],
			"dollal3": money[2]
		})
	print(catnum,qnum)
	return render(request, "jeopardy/question2.html", {
		"catnum": catnum,
		"qnum": qnum,
		"text": questions[int(catnum)+6][int(qnum)],
		"valueP": value,
		"p1": names[0],
		"dollal1": money[0],
		"p2": names[1],
		"dollal2": money[1],
		"p3": names[2],
		"dollal3": money[2]
        })

def question(request, catnum, qnum):
	if(catnum==4 and qnum==3):
		return render(request, "jeopardy/dailyd.html", {
				"catnum": catnum,
				"qnum": qnum,
	       		"text": questions[int(catnum)][int(qnum)],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
	value =200*(int(qnum)+1)
	if request.method == "POST":
		if request.POST.get("correct") == "Correct":
			money[int(request.POST.get("player"))] += value
			return render(request, "jeopardy/single.html", {
				"categories": categories[0:6],
				"questions": questions[0:6],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
			})
		money[int(request.POST.get("player"))] -= int(request.POST.get("valueH"))
		return render(request, "jeopardy/question.html", {
			"catnum": catnum,
			"qnum": qnum,
       		"text": questions[int(catnum)][int(qnum)],
			"valueP": value,
			"p1": names[0],
			"dollal1": money[0],
			"p2": names[1],
			"dollal2": money[1],
			"p3": names[2],
			"dollal3": money[2]
		})
	print(catnum,qnum)
	return render(request, "jeopardy/question.html", {
		"catnum": catnum,
		"qnum": qnum,
		"text": questions[int(catnum)][int(qnum)],
		"valueP": value,
		"p1": names[0],
		"dollal1": money[0],
		"p2": names[1],
		"dollal2": money[1],
		"p3": names[2],
		"dollal3": money[2]
        })
                
def final(request):
	if request.method == "POST":
		if "submitWager" in request.POST:
			return render(request, "jeopardy/finalQ.html", {
				"category": categories[12],
				"text": questions[12][0],
				"wager1": request.POST.get("wager1"),
				"wager2": request.POST.get("wager2"),
				"wager3": request.POST.get("wager3"),
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
        		})
		if "submitQuestion" in request.POST:
        		return render(request, "jeopardy/finalR.html", {
				"category": categories[12],
				"text": questions[12][1],
				"wager1": request.POST.get("wager1"),
				"wager2": request.POST.get("wager2"),
				"wager3": request.POST.get("wager3"),
				"response1": request.POST.get("response1"),
				"response2": request.POST.get("response2"),
				"response3": request.POST.get("response3"),
				"show1": request.session["show1"],
				"show2": request.session["show2"],
				"show3": request.session["show3"],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
        		})
		if request.POST.get("show1") == "true":
			request.session["show1"] = True
		if request.POST.get("show2") == "true":
			request.session["show2"] = True
		if request.POST.get("show3") == "true":
			request.session["show3"] = True
		if request.POST.get("correct") == "Correct":
			money[int(request.POST.get("player"))] += int(request.POST.get("valueH"))
		if request.POST.get("correct") == "Incorrect":
			money[int(request.POST.get("player"))] -= int(request.POST.get("valueH"))
		return render(request, "jeopardy/finalR.html", {
			"category": categories[12],
			"text": questions[12][0],
			"wager1": request.POST.get("wager1"),
			"wager2": request.POST.get("wager2"),
			"wager3": request.POST.get("wager3"),
			"response1": request.POST.get("response1"),
			"response2": request.POST.get("response2"),
			"response3": request.POST.get("response3"),
			"show1": request.session["show1"],
			"show2": request.session["show2"],
			"show3": request.session["show3"],
			"p1": names[0],
			"dollal1": money[0],
			"p2": names[1],
			"dollal2": money[1],
			"p3": names[2],
			"dollal3": money[2]
      		})
        	
	return render(request, "jeopardy/final.html", {
		"category": categories[12],
		"p1": names[0],
		"dollal1": money[0],
		"p2": names[1],
		"dollal2": money[1],
		"p3": names[2],
		"dollal3": money[2]
        })

def dailyd(request):
	if request.method=="POST":
		if "submitWager" in request.POST:
			catnum = request.POST.get("catnum")
			qnum = request.POST.get("qnum")
			value =request.POST.get("wager")
			player = request.POST.get("player")
			print(catnum)
			return render(request, "jeopardy/dailydq.html", {
				"text": questions[int(catnum)][int(qnum)],
				"valueP": value,
				"playerP": player,
				"catnum": int(catnum),
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
        		})
	return render(request, "jeopardy/dailyd.html", {
		"catnum": catnum,
		"qnum": qnum,
		"p1": names[0],
		"dollal1": money[0],
		"p2": names[1],
		"dollal2": money[1],
		"p3": names[2],
		"dollal3": money[2]
        })

def end(request):
	if request.method == "POST":
		if money[0] > money[1] and money[0] > money[2]:
			return render(request, "jeopardy/end.html", {
				"winner": names[0],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
		        })
		if money[1] > money[2] and money[1] > money[0]:
			return render(request, "jeopardy/end.html", {
				"winner": names[1],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
		        })
		if money[2] > money[1] and money[2] > money[0]:
			return render(request, "jeopardy/end.html", {
				"winner": names[2],
				"p1": names[0],
				"dollal1": money[0],
				"p2": names[1],
				"dollal2": money[1],
				"p3": names[2],
				"dollal3": money[2]
		        })
		return render(request, "jeopardy/suddenD.html")
