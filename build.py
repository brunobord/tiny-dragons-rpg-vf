#!/usr/bin/env python
# -*- coding: utf8 -*-
import codecs
import json

import CommonMark
from jinja2 import Environment, FileSystemLoader


if __name__ == '__main__':

    # templates
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.html')
    parser = CommonMark.DocParser()
    renderer = CommonMark.HTMLRenderer()

    # Load pages
    with codecs.open('contents.json', 'r', encoding='utf8') as fd:
        pages = json.load(fd)
    for data in pages:
        with codecs.open("{}.md".format(data['name']), encoding='utf8') as fd:
            content = fd.read()

        ast = parser.parse(content)
        body = renderer.render(ast)

        output = template.render(
            body=body,
            title=data['title']
        )
        with codecs.open('{}.html'.format(data['target']), 'w', encoding='utf8') as fd:
            fd.write(output)
