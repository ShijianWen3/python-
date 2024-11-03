

current_users=['Wen','Su','Li','Zhang','Wang']
new_users=['Wen','Lucy','Jack','Bill','Zhang']
for user in new_users:
    current=[_.lower() for _ in current_users]
    if user.lower() in current:
        print(f'{user}已被使用')
    else:
        print(f'{user}未被使用')

