import os


def get_list_of_persons(file_path):
    result = []
    with open(file_path, 'r') as file_object:
        data = file_object.readlines()
    for person in data:
        item = {
            'name': person.split(',')[0],
            'age': person.split(',')[1].replace('\n', '')
        }
        result.append(item)
    return result


def create_person_file(person_data, person_folder):
    file_path = os.path.join(person_folder, 'info.txt')
    with open(file_path, 'w') as file_object:
        file_object.write(person_data['age'])


def create_folder_and_files(root_folder, person_data):
    person_folder = os.path.join(root_folder, person_data['name'])
    os.makedirs(person_folder)
    create_person_file(person_data, person_folder)


full_path = '/names.txt'
result = get_list_of_persons(full_path)
print(result)
for person in result:
    create_folder_and_files('persons', person)
