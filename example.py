import json, os
from config import ConfigLoader

if __name__ == "__main__":
    loader = ConfigLoader()

    # Load config template
    print("Load 'example/config.yaml.j2'")
    conf = loader.get_config('example/config.yaml.j2')
    print(json.dumps(conf, sort_keys=True, indent=4))

    # Set environment variables
    print("Setting ENV vars")
    os.environ['LOG_LEVEL'] = 'DEBUG'
    os.environ['OBJ1_KEY1'] = 'value1'
    os.environ['OBJ2_KEY2'] = 'value2'

    # `get_config` returns the old config object (static)
    print("Get the old object for 'example/config.yaml.j2'")
    conf = loader.get_config('example/config.yaml.j2')
    print(json.dumps(conf, sort_keys=True, indent=4))

    # Use `True` flag to force reload the template
    print("Recompile 'example/config.yaml.j2' for new ENV vars")
    conf = loader.get_config('example/config.yaml.j2', True)
    print(json.dumps(conf, sort_keys=True, indent=4))