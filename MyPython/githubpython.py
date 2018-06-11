import github3

try:
    # Python 2
    prompt = raw_input
except NameError:
    # Python 3
    prompt = input

def my_two_factor_function():
    code = ''
    while not code:
        # The user could accidentally press Enter before being ready,
        # let's protect them from doing that.
        code = prompt('Enter 2FA code: ')
    return code

username = ''
password = ''

while not username:
    username = prompt('Enter Username: ')

while not password:
    password = prompt('Enter Password: ')    

gh = github3.login(username, password=password,two_factor_callback=my_two_factor_function)

sigmavirus24 = gh.me()

repo = gh.repositories(type='owner')
myList = list(repo)

print myList.__len__()

for t in repo:
    print t.branches

print sigmavirus24.name
