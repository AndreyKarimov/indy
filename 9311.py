import json

def search_women(file_name: str) -> None:
    id_and_count = []
    with open(file_name, encoding='UTF-8') as file:
        data = json.load(file)
        for group in data:
            id_and_count.append((group['id_group'], len([person for person in group['people']
                                                         if person['gender'] == 'Female' and person['year'] > 1977])))
    print(*sorted(id_and_count, key=lambda x: -x[1])[0])
search_women('group_people.json')
