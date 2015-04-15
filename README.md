# cuescience-design

## Installation
1. 'cuescience_design' to installed apps _above_ the django admin.
2. Add "cuescience_design.processor.admin_caption" to your TEMPLATE_CONTEXT_PROCESSORS
3. Add the following constants to your settings.py:
PROJECT_VERSION = "1.0"
PROJECT_NAME = "Your Project Name"
PROJECT_COLOR = (r, g, b) # your admin color as rgb triple
