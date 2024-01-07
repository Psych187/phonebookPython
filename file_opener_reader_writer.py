def create_new_contact(file_name):
    information = []
    current_id = count_contact(file_name)
    information.append(str(current_id))
    information.append(input("Enter name: "))
    information.append(input("Enter phone num: "))
    information.append(input("Enter group: "))
    with open (file_name, 'a') as file:
        file.write(';'.join(information)+"\n")

def convert_file_to_dict(file_name):
    contacts={}
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            print(line.split(';'))
    return contacts
def count_contact(file_name):
    lines = 0
    with open(file_name, 'r') as file:
        for i in file:
            lines += 1
    return lines
def show_contacts(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
def change_contact_information(file_name):
    pass