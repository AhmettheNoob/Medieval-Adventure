# app.py
from flask import Flask, render_template, request, redirect, url_for
from game import Character, Shop, Kingdom

app = Flask(__name__)
character = Character(name="Hero")
shop = Shop()

@app.route('/')
def index():
    status = character.show_status()
    return render_template('index.html', status=status, shop=shop)

@app.route('/choose_route', methods=['POST'])
def choose_route():
    route = request.form['route']
    message = character.choose_route(route)
    return redirect(url_for('index', message=message))

@app.route('/gather_gold', methods=['POST'])
def gather_gold():
    amount = int(request.form['amount'])
    message = character.gather_gold(amount)
    return redirect(url_for('index', message=message))

@app.route('/fight')
def fight():
    message = character.fight()
    return redirect(url_for('index', message=message))

@app.route('/level_up')
def level_up():
    message = character.level_up()
    return redirect(url_for('index', message=message))

@app.route('/buy_bloodline', methods=['POST'])
def buy_bloodline():
    bloodline_name = request.form['bloodline']
    bloodline_obj = next((b for b in shop.bloodlines if b.name == bloodline_name), None)
    if bloodline_obj and character.gold >= bloodline_obj.cost:
        character.bloodline = bloodline_obj
        character.gold -= bloodline_obj.cost
        message = f"Bought bloodline: {bloodline_obj.name} ({bloodline_obj.purity})"
    else:
        message = "Not enough gold or invalid bloodline."
    return redirect(url_for('index', message=message))

@app.route('/found_kingdom', methods=['POST'])
def found_kingdom():
    name = request.form['name']
    if not character.kingdom:
        character.kingdom = Kingdom(name, character)
        message = f"Founded kingdom: {name}"
    else:
        message = "You already have a kingdom."
    return redirect(url_for('index', message=message))

@app.route('/develop_city')
def develop_city():
    if character.kingdom:
        message = character.kingdom.develop_city()
    else:
        message = "You don't have a kingdom yet."
    return redirect(url_for('index', message=message))

@app.route('/manage_resources', methods=['POST'])
def manage_resources():
    if character.kingdom:
        resource_type = request.form['resource_type']
        amount = int(request.form['amount'])
        message = character.kingdom.manage_resources(resource_type, amount)
    else:
        message = "You don't have a kingdom yet."
    return redirect(url_for('index', message=message))

if __name__ == "__main__":
    app.run(debug=True)
