from homework9.decorators import html_template


@html_template
def greetings(name):
    return f"Hello {name}"


greetings("Max")
