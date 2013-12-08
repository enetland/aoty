from mako.template import Template
from mako.lookup import TemplateLookup
from aoty import *


def run(output_file_name):
  lookup = TemplateLookup(directories=['./templates'])
  page = Template(filename='./templates/album_list.mako', lookup=lookup)

  with open(output_file_name, 'w') as f:
    f.write(page.render(albums=Album.select(),
                        tags = popular_tags()).encode('utf8'))