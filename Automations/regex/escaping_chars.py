import re

# no escaping
print(re.search(r'.com', 'welcome'))
# escaping the .
print(re.search(r'\.com', 'welcome'))
# escaping the .
print(re.search(r'\.com', 'mydomain.com'))

# using \w*
print(re.search(r'\w*', 'This is an example'))
# using \w*
print(re.search(r'\w*', 'And_this_is_another'))
