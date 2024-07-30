# Install virtualenv if not already installed
pip install virtualenv

# Create the virtual environment
cd ex02
virtualenv venv

# Activate the virtual environment
# On Windows
# venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

# Install required packages
pip install -r requirement.txt

# Run your script
python request_wikipedia.py "Albert Einstein"

# Deactivate the virtual environment when done
deactivate