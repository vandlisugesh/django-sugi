from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

def welcome(request):
	print "WELCOME", request.method
	return render(request, "currency_application/welcome.html", {})

def form_data(request):
	if not request.user.is_authenticated() or request.user == "AnonymousUser":
		return redirect('accounts/login/')
	notes_dict = {}
	coins_dict = {}
	notes_list = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
	coins_list = [50, 25, 10, 1]
	if request.method == "GET":
		form = InputForm()
		context = {
		"form" : form
		}
		return render(request, "currency_application/forms.html", context)
	else:
		form = InputForm(request.POST or None)
		if form.is_valid():
			if request.user != "AnonymousUser":
				input_value = form.cleaned_data.get("input_value", None)
				if isinstance(input_value, float):
					context = {
					"int_part" : int(str(input_value).split(".")[0]),
					"decimal_part" : int(str(input_value).split(".")[1])
					}
				else:
					context = {
					"int_part" : input_value,
					"decimal_part" : 0
					}
				if context["int_part"]:
					int_part = context["int_part"]
					for item in notes_list:
						if int_part/item != 0:
							notes_dict[item] = int_part/item
							int_part = int_part % item
						else:
							notes_dict[item] = 0
				if context["decimal_part"]:
					decimal_part = context["decimal_part"]
					for item in coins_list:
						if decimal_part/item != 0:
							coins_dict[item] = decimal_part/item
							decimal_part = decimal_part % item
						else:
							coins_dict[item] = 0
				context.update({"notes_dict":notes_dict, "coins_dict":coins_dict, "notes_list":notes_list, "coins_list":coins_list, "form":form})
				return render(request, "currency_application/output.html", context)
		else: return render(request, "currency_application/output.html", {"form":form})

