import re


def findEmailDomain(address):
    return re.findall("@([^@]+$)", address)[0]


def findEmailDomain(address):
    return address.split("@")[-1]


def findEmailDomain(address):
    return re.search("@\w.+", address).group()[1:]


# test
address = "prettyandsimple@example.com"
print(findEmailDomain(address))

# test
address = '<>[]:,;@"!#$%&*+-/=?^_{}| ~.a"@example.org'
print(findEmailDomain(address))

# test
address = "someaddress@yandex.ru"
print(findEmailDomain(address))

# test
address = '" "@xample.org'
print(findEmailDomain(address))
