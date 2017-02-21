import re
import textwrap


def format_text(text):
    return textwrap.dedent(text)

def is_latin(text):
    rule = re.compile(r'^[A-Za-z0-9]*$')
    return rule.match(text) != None
