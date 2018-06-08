import os
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import WithDataTemplateView

"""This is where the URLS for DWebSummit are defined

To make things a little more automatic, we parse the directory and generate
URLS for each index.html file
For example
    dwebsummit/index.html  => /
    dwebsummit/logistics/index.html => /logistics/
"""

def remove_prefix(text, prefix):
    """Removes a prefix from a string"""
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def build_url(rootdir, root, file):
    """Builds a django url from directory arguments
    example return value:
        url(r'^logistics/?$', TemplateView.as_view(template_name="dwebsummit/logistics.html")),
    """
    template_dir = os.path.basename(rootdir)
    parent = remove_prefix(root, rootdir).strip('/')

    if parent == '':
        title = 'home'
        pattern = r'^$'
        full_file = template_dir + '/' + file
    else:
        title = parent.replace('/', '-')
        pattern = r'^' + parent + '/$'
        full_file = template_dir + '/' + parent + '/' + file

    view = WithDataTemplateView.as_view(template_name=full_file, title=title)
    return url(pattern, view)


def build_url_patterns_from_templates(urlpatterns):
    rootdir = os.path.join(os.path.dirname(__file__), 'templates', 'dwebsummit')
    for root, subdirs, files in os.walk(rootdir):
        for file in files:
            if file == 'index.html':
                urlpatterns.append(build_url(rootdir, root, file))


urlpatterns = []

# Note, non-file-based patterns can be added here before the function call
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


build_url_patterns_from_templates(urlpatterns)
