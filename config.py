from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml
import os

class ConfigLoader():
  # ============ "PRIVATE" Code ============

  # Static class variable '_config' holds the JSON of the templated YAML
  _config = None
  _filepath = None

  def __init__(self):
    self.env = Environment(
      cache_size=0,  # Recompile every time
      auto_reload=True,  # Check location for changes to files
      loader=FileSystemLoader(searchpath='./'),
      autoescape=select_autoescape(['html', 'xml'])
    )
    # Add custom filter to Jinja2 to replace placeholders with ENV vars
    self.env.filters['env_templated'] = \
      lambda default_val, var_name: os.getenv(var_name, default_val)

  def _generate_config(self):
    template = self.env.get_template(self._filepath)
    self._config = yaml.safe_load(template.render())

  # ============ "PUBLIC" Code ============
  def get_config(self, _filepath, force_reload=False):
    if force_reload == True or self._filepath != _filepath:
        self._filepath = _filepath
        self._generate_config()

    return self._config
