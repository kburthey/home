#! Python3

from jinja2 import Environment

HTML = """
<html>
<head>
<title>{{title}}</title>
</head>
<body>

Test

</body>
</html>
"""

def print_html_doc():
    fname = "gist.html"
    with open(fname, 'w') as f:
        html_out = Environment().from_string(HTML).render(title='Hellow Gist')
        f.write(html_out)

if __name__ == '__main__':
    print_html_doc()
