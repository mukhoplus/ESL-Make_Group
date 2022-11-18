import random

GROUP_NUMBER = 2
USERS = []

def main():
    groups = [[] for _ in range(GROUP_NUMBER)]
    make_group(random.sample(USERS, len(USERS)), groups)
    show_info(groups)

def make_group(users, groups):
    while len(users) > 0:
        user = random.choice(users)
        group = choice_group(groups)
        if add_user_in_group(group, user):
            delete_user_in_users(users, user)

def choice_group(groups):
    numbers = [i for i in range(GROUP_NUMBER)]
    return groups[random.choice(numbers)]

def check_number(group):
    return len(group) < round(len(USERS)/GROUP_NUMBER, 0)

def add_user_in_group(group, user):
    if check_number(group):
        group.append(user)
        return True
    return False

def delete_user_in_users(users, user):
    users.remove(user)

def make_line():
    print("---------------------------------------")

def show_info(groups):
    make_line()
    for i in range(len(groups)):
        print("A조:" if i == 0 else "B조:", end=' ')
        show_group(groups[i])
        make_set(groups[i])
        make_line()

def show_group(group):
    print(*group, sep=', ')

def make_set(group):
    print("- 1경기: " + group[0] + " vs " + group[1] + " || 투혼")
    print("- 2경기: " + group[1] + " vs " + group[2] + " || 이클립스")
    print("- 3경기: " + group[2] + " vs " + group[0] + " || 폴리포이드")

main()
