import os

# In Terminal, run the following commands to set the environment variables
# export IFREMER_USERNAME='your_ifremer_username'
# export IFREMER_PASSWORD='your_ifremer_password'
# export CMEMS_USERNAME='your_cmems_username'
# export CMEMS_PASSWORD='your_cmems_password'
# export SWOT_USERNAME='your_swot_username'
# export SWOT_PASSWORD='your_swot_password'

# Read login details from environment variables
# ifremer_username = os.environ.get('IFREMER_USERNAME')
# ifremer_password = os.environ.get('IFREMER_PASSWORD')
cmems_username = os.environ.get('CMEMS_USERNAME')
cmems_password = os.environ.get('CMEMS_PASSWORD')
swot_username = os.environ.get('SWOT_USERNAME')
swot_password = os.environ.get('SWOT_PASSWORD')

# Define the class SecretCodes
class SecretCodes:
    def __init__(self, ifremer_username=None, ifremer_password=None, cmems_username=None, cmems_password=None, swot_username=None, swot_password=None):
        self.ifremer_username = ifremer_username
        self.ifremer_password = ifremer_password
        self.cmems_username = cmems_username
        self.cmems_password = cmems_password
        self.swot_username = swot_username
        self.swot_password = swot_password

# Create an instance of SecretCodes
secretcodes = SecretCodes(cmems_username = cmems_username, cmems_password = cmems_password, swot_username = swot_username, swot_password = swot_password)