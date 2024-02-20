class SecretCodes:
    def __init__(self, ifremer_username=None, ifremer_password=None, cmems_username=None, cmems_password=None, swot_username=None, swot_password=None):
        self.ifremer_username = ifremer_username
        self.ifremer_password = ifremer_password
        self.cmems_username = cmems_username
        self.cmems_password = cmems_password
        self.swot_username = swot_username
        self.swot_password = swot_password

# Create an instance of SecretCodes
secretcodes = SecretCodes(cmems_username = "mromero4", cmems_password = "Glasgow10!!!",
                          swot_username = "mattiaromero10@gmail.com", swot_password = "phDCLB"
) 

