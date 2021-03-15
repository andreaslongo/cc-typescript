import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "[Error] The project slug (%s) is not a valid module name. Please use '_' instead of '-'."
        % module_name
    )
    sys.exit(1)
