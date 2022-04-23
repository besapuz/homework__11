import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf8') as file:
        user_d = json.load(file)
    return user_d


user_dict = load_candidates_from_json()


def search_id(index):
    """Ищет пользователя по id"""
    for r in user_dict:
        if index == r["id"]:
            return r


def add_skills_dict(sk):
    """Выполняет поиск навыков в skills"""
    skill_dict = []
    sk = sk.lower()
    for value in user_dict:
        b = value["skills"].lower().split(", ")
        if sk in b:
            skill_dict.append(value)
    return skill_dict


def get_candidates_by_name(name):
    """возвращает пользователя по Name"""
    name = name.lower()
    name_dict = []
    for value in user_dict:
        b = value["name"].lower()
        if name in b:
            name_dict.append(value)
    return name_dict


