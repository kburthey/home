#! Python3

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_file, context):
    return TEMPLATE_ENVIRONMENT.get_template('index.html').render(context)

def create_index_html():
    fname = "output.html"
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    text = ['hello', 'world']
    context = {
        'urls':urls,
        'text':text
        }
    #
    with open(fname, 'w') as f:
        html = render_template('index.html', context)
        f.write(html)


def main():
    create_index_html()

######

if __name__ == "__main__":
    main()

    
