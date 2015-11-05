from django import forms

class InputForm(forms.Form):
	input_value = forms.CharField(required=True, label="Enter the amount in numbers")

	def clean_input_value(self):
		input_value = self.cleaned_data.get("input_value")
		if not input_value.isdigit():
			if "." in input_value:
				if not input_value.replace('.','',1).isdigit():
					raise forms.ValidationError("The entered amount is not valid")
			else:
				raise forms.ValidationError("The entered amount is not valid")
		if "." in input_value:
			return float(input_value)
		else: return int(input_value)