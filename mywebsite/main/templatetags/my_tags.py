from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def increment(context):
    """
    Функция, которая увеличивает счетчик на 1 при каждом вызове и сбрасывает его при обновлении страницы.
    """
    request = context['request']
    if not hasattr(request, 'increment_counter'):
        request.increment_counter = 0
    request.increment_counter += 1
    return request.increment_counter
