from django.shortcuts import render
from django.views.generic import View

class Formulario1(View):
	template_name = 'formulario1/formulario1-1.html'

	def get(self, request):
		print(request)

		return render(request, self.template_name)