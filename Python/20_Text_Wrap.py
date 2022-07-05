import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    new_string = wrapper.fill(text=string)
    return new_string
