from re import findall


class NameTooShort(Exception):
    pass


class MustContainAtSymbol(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneATSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4
pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'
valid_domains = [".com", ".bg", ".net", ".org"]
email = input()

while email != "End":
    try:
        if email.count('@') > 1:
            raise MoreThanOneATSymbol("Email should contain only one @!")
        if len(email.split("@")[0]) <= MIN_LENGTH:
            raise NameTooShort(f"Name must be more than {MIN_LENGTH} characters")
        if len(findall(pattern_name, email)[0]) != len(email.split("@")):
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots.")
        if "@" not in email:
            raise MustContainAtSymbol("Email must contain @")
        if findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f"Domain must be one of the following: {','.join(valid_domains)}")
        print("Email is valid")
    except IndexError:
        print("Invalid email!")

    email = input()
