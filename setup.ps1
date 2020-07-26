# Create and enable a virtual environment
python -m venv env

.\env\scripts\activate.ps1

# Upgrade pip and install required packages
pip install --upgrade pip
pip install -r requirements.txt

# Create a .env file from the .env.template
if (-not (test-path .env)) 
{
    Copy-Item .env.template .env
}