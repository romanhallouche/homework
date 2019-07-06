

import glob
import os
from jinja2 import Template

###########################################################################

all_html_files = glob.glob("content/*.html")
output = glob.glob("docs/*.html")
base = open('templates/base.html').read()


pages = []





def pages_in_html():
    for page in all_html_files:
        page_content = os.path.basename(page)
        name_only, extension = os.path.splitext(page_content)

        pages.append({
            "filename": page,
            "title": name_only,
            "output": page_content,
        })



def run_all_pages():
    for page in pages:
        page_content = open(page["filename"]).read()
        title = page['title']
        filename = page['filename']

        template = Template(base)
        final_page = template.render(title=title, content=page_content, pages=pages)

        output_filename = "docs/" + page["output"]
        open(output_filename, "w+").write(final_page)