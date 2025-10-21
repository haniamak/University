from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

template = env.get_template("z4.j2")

users = [
    {"username": "ala", "url": "/user/ala"},
    {"username": "bob", "url": "/user/bob"},
]

html = template.render(users=users)
print(html)