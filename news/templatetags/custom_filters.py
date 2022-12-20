from django import template


register = template.Library()

stop_words = [
    'Cyberpunk',
    '2077',
]



@register.filter(name='censor')

def censor(value):

    for sw in stop_words:
        value = value.replace(sw, sw[0] + '*' * len(sw))
    return value









