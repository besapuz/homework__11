from flask import Flask, render_template
from funk import search_id, add_skills_dict, load_candidates_from_json, get_candidates_by_name

app = Flask(__name__)


@app.route("/")
def return_index():
    user_dict = load_candidates_from_json()
    return f"{render_template('list.html', user=user_dict)}"


@app.route("/candidate/<int:index>")
def outputs_user(index):
    user_id = search_id(index)
    return render_template('single.html', user_name=user_id)


@app.route("/skill/<string:skill>")
def user_skill(skill):
    skills = add_skills_dict(skill)
    return render_template('skills.html', skills=skills, skill=skill, len_skills=len(skills))


@app.route("/search/<name>")
def outputs_user_name(name):
    name = name.lower()
    user_name = get_candidates_by_name(name)
    len_user = len(user_name)
    return render_template('search.html', user_name=user_name, len_user=len_user)


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)
