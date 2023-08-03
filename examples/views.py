from django.http import HttpResponse
from django.shortcuts import render


# request = HttpRequest()
def test_view(request):
    return HttpResponse("Test")


def test_view_hello(request):
    return HttpResponse("Hello", status=500)


def test_view_bye(request):
    return HttpResponse("Goodbye")


# Отправляем объекты python
# def test_view(request):
#     my_list = [1, 2, "3", 4]
#     return HttpResponse(my_list)


# Маленький кусок html
# def test_view(request):
#     html = "<h1>Этот текст будет полужирным, <i>а этот — ещё и курсивным</i>.</h1>"
#     return HttpResponse(html)


# Большой кусок html
# def test_view(request):
#     html = """<!DOCTYPE html>
# <html lang="ru">
#    <head>
#       <meta charset="UTF-8">
#       <title>TEST VIEW</title>
#    </head>
#    <body>
#       <p>
#          <b>
#             Этот текст будет полужирным, <i>а этот — ещё и курсивным</i>.
#          </b>
#       </p>
#    </body>
# </html>"""
#     return HttpResponse(html)

# Отправляем заголовки и меняем статус ответа
# def test_view(request):
#     my_list = [1, 2, "3", 4]
#     headers = {"Name": "Azamat"}
#     return HttpResponse(my_list, headers=headers, status=404)

# Обрабатываем динамический эндпоинт с числом
def catch_number_view(request, number):
    return HttpResponse(f"Your number: {number}")


# Обрабатываем динамический эндпоинт со строкой
def catch_string_view(request, string):
    return HttpResponse(f"Your string: {string}")
