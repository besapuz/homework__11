from flask import Flask, render_template
from funk import search_id, add_skills_dict, get_json, get_candidates_by_name

app = Flask(__name__)

user_dict = get_json()


@app.route("/")
def return_index():
    return f"<h1>Гавная страница</h1> {render_template('home.html', user=user_dict)}"


@app.route("/candidate/<int:index>")
def outputs_user(index):
    user_id = search_id(index)
    skills = user_id["skills"]
    name = user_id["name"]
    position = user_id["position"]
    picture = user_id["picture"]
    return f"<h1>{name}</h1><p>{position}</p><img src={picture} width=200/><p>\n\n{skills}</p>"


@app.route("/skills/<string:skill>")
def user_skill(skill):
    skills = get_candidates_by_name(skill)
    return render_template('skills.html', skills=skills, skill=skill, len_skills=len(skills))


@app.route("/search/<name>")
def outputs_user_name(name):
    name = name.lower()
    user_name = get_candidates_by_name(name)
    len_user = len(user_name)
    return render_template('search.html', user_name=user_name, len_user=len_user)


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)
