def sort_by_value(item):
    return item['age']


def get_youngest_names(persons):
    result = []
    # sort_age = sorted(persons, key=lambda item: item["age"], reverse=False)
    sort_by_ages = sorted(persons, key=sort_by_value, reverse=False)
    # print(sort_by_ages)
    for person in sort_by_ages:
        if person.get("age") == sort_by_ages[0].get("age"):
            # print(person.get("name"))
            result.append(person.get("name"))
    return result


def get_youngest_names2(persons):
    ages = [i['age'] for i in persons]
    names = [i['name'] for i in persons if i['age'] == min(ages)]
    return names


def get_longest_names(persons):
    names_len = [len(i['name']) for i in persons]
    names = [i['name'] for i in persons if len(i['name']) == min(names_len)]
    return names


def get_average_age(persons):
    sum_age = 0
    for person in persons:
        sum_age += person.get("age")
    if len(persons) > 0:
        result = sum_age / len(persons)
    else:
        print('Empty list')
        result = None

    # ages = [i['age'] for i in persons]
    # result = sum(ages) / len(ages) if len(ages) > 0 else None
    return result


if __name__ == '__main__':
    persons = [
        {"name": "Jacky", "age": 35},
        {"name": "John", "age": 15},
        {"name": "Jack", "age": 45}
    ]
    print(f'Task 1-a: {get_youngest_names(persons)}')
    print(f'Task 1-b: {get_longest_names(persons)}')
    print(f'Task 1-c: {get_average_age(persons)}')

    my_dict = {i: i ** 2 for i in range(1, 10, 2)}
    my_dict1 = {i: i ** 2 for i in range(2, 10, 3)}


