import json


def get_json():
    with open('candidates.json', 'r', encoding='utf8') as file:
        user_d = json.load(file)
    return user_d


user_dict = get_json()


def search_id(index):
    """Ищет пользователя по id"""
    for r in range(len(user_dict)):
        if index is user_dict[r]["id"]:
            c = user_dict[r]
            return c


def add_skills_dict(sk):
    """Выполняет поиск навыков в skills"""
    skill_dict = []
    sk = sk.lower()
    for value in user_dict.values():
        b = value["skills"].lower()
        s = b.split(", ")
        if sk in s:
            skill_dict.append(value)
    return skill_dict


def get_candidates_by_name(sk):
    """возвращает пользователя по Name"""
    skill_dict = []
    sk = sk.lower()
    for value in user_dict:
        b = value["skills"].lower()
        s = b.split(", ")
        if sk in s:
            skill_dict.append(value)
    return skill_dict
