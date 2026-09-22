#currently only testing

import requests

url = "https://www.imf.org/external/datamapper/api/v2/NGDP_RPCH/"

data = requests.get(url).json()

indicators = data["indicators"]
# Real GDP growth for Austria
obs = data["values"]["NGDP_RPCH"]["AFG"]

print(indicators)
print(obs)