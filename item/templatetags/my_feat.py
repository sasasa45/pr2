from django import template

register=template.Library()

@register.filter(name='stars')
def stars(value):
    suma=0
    group=value.rate_set.all()
    for part in group:
        suma+=part.rate
    coef=round(suma/group.count())
    str_star=[]
    for i in range(1,6):
        if i<=coef:
            str_star.append(9733)
        else:
            str_star.append(9734)

    return [str_star, group.count()]
