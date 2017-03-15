import re
import textwrap


def format_text(text):
    return textwrap.dedent(text)


def is_latin(text):
    rule = re.compile(r'[aA-zZ]')
    return rule.match(text) is not None


def is_cyrillic(text):
    rule = re.compile(r'[аА-яЯ]')
    return rule.match(text) is not None
