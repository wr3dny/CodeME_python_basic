with open('mail_list.txt') as fopen:
    content = fopen.readlines(1)
    content = content.remove("\'")

print(content)

user_mail = input('Give Your email: ')
while user_mail not in content:
    user_mail = input('Give Your email: ')
else:
    print('Your mail on the list !')

