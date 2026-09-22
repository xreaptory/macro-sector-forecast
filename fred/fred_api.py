from fredapi import Fred

fred = Fred(api_key="92b041d35c6d3271bfc7e98c948b83dc")

# Pull US GDP
gdp = fred.get_series("GDP")
print(gdp.tail())

# Pull unemployment rate
unemployment = fred.get_series("UNRATE")
print(unemployment.tail())