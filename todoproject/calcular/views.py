from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sumar(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse(f"La suma de {num1} + {num2} = {resultado}")

@csrf_exempt
def restar(request, num1, num2):
    resultado = num1 - num2
    return HttpResponse(f"La resta de {num1} - {num2} = {resultado}")

@csrf_exempt
def multiplicar(request, num1, num2):
    resultado = num1 * num2
    return HttpResponse(f"La multiplicación de {num1} * {num2} = {resultado}")
