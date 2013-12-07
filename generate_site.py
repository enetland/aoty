from mako.template import Template
from mako.lookup import TemplateLookup
from aoty import *

lookup = TemplateLookup(directories=['./templates'])
page = Template(filename='./templates/album_list.mako', lookup=lookup)

print page.render(albums=Album.select())