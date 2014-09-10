import operator
from django.conf import settings


def admin_caption(request):
    try:
        color = settings.PROJECT_COLOR
        version = settings.PROJECT_VERSION
        project_name = settings.PROJECT_NAME
    except AttributeError:
        error_message = 'PROJECT_NAME, PROJECT_VERSION and PROJECT_COLOR seems to be missing in your settings.py.' \
                        ' Please specify these values.'
        raise (RuntimeError(error_message))

    highlight_color = map(operator.sub, color, (25, 25, 25))
    highlight_color = map(max, highlight_color, (0, 0, 0))
    highlight_color = tuple(highlight_color)
    result = {'project_caption': project_name, 'project_version': version,
              'project_color': color, 'project_highlight_color': highlight_color, }

    return result