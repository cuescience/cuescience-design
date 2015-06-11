# cuescience-design

## Installation
1. Add `git+https://github.com/cuescience/cuescience-design#egg=cuescience-design` to your `requirements.txt`
2. `'cuescience_design'` to installed apps _above_ the django admin.
2. Add `"cuescience_design.processor.admin_caption"` to your `TEMPLATE_CONTEXT_PROCESSORS` (when using django 1.8 use `context_processors` in the `TEMPLATES` configuration)
3. Add the following constants to your `settings.py`:
```python
PROJECT_VERSION = "1.0"
PROJECT_NAME = "Your Project Name"
PROJECT_COLOR = (r, g, b) # your admin color as rgb triple
´´´
