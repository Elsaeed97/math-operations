from django.shortcuts import render

# Create your views here.

def home(request):
	context = {

	}
	return render(request, 'home.html', context)

def add(request):
	from random import randint 
	num_1 = randint(0 , 10 )
	num_2 = randint(0 , 10 )
	if request.method == 'POST':
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')

		if not answer:
			my_answer = "You Forgot to Answer !!"
			alert = "danger"
			return render(request, 'add.html' ,{
				'answer' : answer,
				'my_answer' : my_answer,
				'num_1' : num_1,
				'num_2' : num_2,
				'alert' : alert,
				})

		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct : " + old_num_1 + " + " + old_num_2 + " Is "  + answer
			alert = "success"
		else : 
			my_answer = "Incorrect :  " + old_num_1 + " + " + old_num_2 + " Is Not  " + answer  + " It's "+ str(correct_answer)
			alert = "danger"
		context = {
			'answer' : answer,
			'my_answer' : my_answer,
			'num_1' : num_1,
			'num_2' : num_2,
			'alert' : alert
		}
		return render(request, 'add.html', context)
	else:
		context = {
			'num_1' : num_1,
			'num_2' : num_2,
		}
		return render(request, 'add.html', context)

def subtract(request):
	from random import randint 
	num_1 = randint(0 , 10 )
	num_2 = randint(0 , 10 )
	if request.method == 'POST':
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')

		if not answer:
			my_answer = "You Forgot to Answer !!"
			alert = "danger"
			return render(request, 'subtract.html' ,{
				'answer' : answer,
				'my_answer' : my_answer,
				'num_1' : num_1,
				'num_2' : num_2,
				'alert' : alert
				})

		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct : " + old_num_1 + " - " + old_num_2 + " Is "  + answer
			alert = "success"
		else : 
			my_answer = "Incorrect :  " + old_num_1 + " - " + old_num_2 + " Is Not  " + answer  + " It's "+ str(correct_answer)
			alert = "danger"
		context = {
			'answer' : answer,
			'my_answer' : my_answer,
			'num_1' : num_1,
			'num_2' : num_2,
			'alert' : alert
		}
		return render(request, 'subtract.html', context)
	else:
		context = {
			'num_1' : num_1,
			'num_2' : num_2,
		}
		return render(request, 'subtract.html', context)


def multiply(request):
	from random import randint 
	num_1 = randint(0 , 10 )
	num_2 = randint(0 , 10 )
	if request.method == 'POST':
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')

		if not answer:
			my_answer = "You Forgot to Answer !!"
			alert = "danger"
			return render(request, 'multiply.html' ,{
				'answer' : answer,
				'my_answer' : my_answer,
				'num_1' : num_1,
				'num_2' : num_2,
				'alert' : alert
				})

		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct : " + old_num_1 + " * " + old_num_2 + " Is "  + answer
			alert = "success"
		else : 
			my_answer = "Incorrect :  " + old_num_1 + " * " + old_num_2 + " Is Not  " + answer  + " It's "+ str(correct_answer)
			alert = "danger"
		context = {
			'answer' : answer,
			'my_answer' : my_answer,
			'num_1' : num_1,
			'num_2' : num_2,
			'alert' : alert
		}
		return render(request, 'multiply.html', context)
	else:
		context = {
			'num_1' : num_1,
			'num_2' : num_2,
		}
		return render(request, 'multiply.html', context)


def devide(request):
	from random import randint 
	num_1 = randint(0 , 10 )
	num_2 = randint(1, 10 )
	if request.method == 'POST':
		answer = request.POST.get('answer')
		old_num_1 = request.POST.get('old_num_1')
		old_num_2 = request.POST.get('old_num_2')

		if not answer:
			my_answer = "You Forgot to Answer !!"
			alert = "danger"
			return render(request, 'devide.html' ,{
				'answer' : answer,
				'my_answer' : my_answer,
				'num_1' : num_1,
				'num_2' : num_2,
				'alert' : alert
				})

		correct_answer = int(old_num_1) / int(old_num_2)
		if float(answer) == correct_answer:
			my_answer = "Correct : " + old_num_1 + " / " + old_num_2 + " Is "  + answer
			alert = "success"
		else : 
			my_answer = "Incorrect :  " + old_num_1 + " /" + old_num_2 + " Is Not  " + answer  + " It's "+ str(correct_answer)
			alert = "danger"
		context = {
			'answer' : answer,
			'my_answer' : my_answer,
			'num_1' : num_1,
			'num_2' : num_2,
			'alert' : alert
		}
		return render(request, 'devide.html', context)
	else:
		context = {
			'num_1' : num_1,
			'num_2' : num_2,
		}
		return render(request, 'devide.html', context)



