from jinja2 import Environment
from django_browser_reload.jinja import django_browser_reload_script


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            # ...
            "django_browser_reload_script": django_browser_reload_script,
        }
    )
    return env
