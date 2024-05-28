from django import template

register = template.Library()

class ChangeStatementNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        status = context.get(self.var_name, False)
        context[self.var_name] = not status
        return ''

@register.tag
def change_statement(parser, token):
    try:
        tag_name, var_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("tag requires a single argument")
    return ChangeStatementNode(var_name)