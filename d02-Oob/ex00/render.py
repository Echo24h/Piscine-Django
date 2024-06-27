import sys
import re


def render_template(template_path, settings):
    # Read the template file
    try:
        with open(template_path, 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file {template_path} does not exist.")
        sys.exit(1)

    # Replace the patterns with settings values
    for key, value in settings.items():
        template_content = re.sub(r'\{' + key + r'\}', str(value), template_content)

    # Write the output to an HTML file
    output_path = re.sub(r'\.template$', '.html', template_path)
    with open(output_path, 'w') as file:
        file.write(template_content)

    print(f"The file has been rendered to {output_path}")


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <template-file>")
        sys.exit(1)

    template_path = sys.argv[1]

    # Check the file extension
    if not template_path.endswith('.template'):
        print("Error: The template file must have a .template extension.")
        sys.exit(1)

    # Import the settings from settings.py
    try:
        import settings
        settings_dict = {attr: getattr(settings, attr) for attr in dir(settings) if not callable(getattr(settings, attr)) and not attr.startswith("__")}
    except ImportError:
        print("Error: Could not import settings.py")
        sys.exit(1)

    render_template(template_path, settings_dict)