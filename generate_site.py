from mako.template import Template
from mako.lookup import TemplateLookup
from aoty import *

lookup = TemplateLookup(directories=['./templates'])
page = Template(filename='./templates/album_list.mako', lookup=lookup)

with open('index.html', 'w') as f:
  f.write(page.render(albums=Album.select()).encode('utf8'))