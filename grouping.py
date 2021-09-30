
pairs = dict()
while True:
    add_members = []
    number_of_members = int(input("enter the total number of members in your group or 0 to exit: "))

    if number_of_members <= 0:
        break
    group_number = input("enter your group number: ")
    for i in range(number_of_members):

        list_members = input("enter list of members in your group: ")
        add_members.append(list_members)
        pairs[group_number] = add_members
        print("group successfully added")

        print(pairs)

















