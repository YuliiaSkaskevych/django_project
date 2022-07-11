from math import sqrt

from django.shortcuts import render

from triangle.forms import triangle_form


def triangle_calculate(request):
    if request.method == "POST":
        t_form = triangle_form(request.POST)
        if t_form.is_valid():
            a = t_form.cleaned_data['leg_1']
            b = t_form.cleaned_data['leg_2']
            hypotenuse = sqrt(a**2+b**2)
            return render(request,
                          "triangle/index.html",
                          {
                              'hypotenuse': round(hypotenuse, 2),
                              "t_form": t_form,
                          })
    else:
        t_form = triangle_form(request.POST)
    return render(request,
                  "triangle/index.html",
                  {
                      'hypotenuse': None,
                      "t_form": t_form,
                  })
