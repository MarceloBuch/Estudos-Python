from flask import Flask, make_response, jsonify
import json
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'dbFifa'
)

@app.route('/players/id/<id_player>')
def get_player_by_id(id_player):
    cursor = conn.cursor(buffered=True)

    sql = f"SELECT * FROM male_players WHERE ID = '{id_player}'"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    json_data = []
       
    if data:
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)
    else:
        return make_response(jsonify({'message': 'Jogador não encontrado'}), 404)


@app.route('/players/nation/<nation_name>', methods = ['GET'])
def get_players_by_nation(nation_name):
    cursor = conn.cursor(buffered=True)

    sql = f"SELECT * FROM male_players WHERE Nation like '%{nation_name}%';"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    json_data = []
       
    if data:
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)
    else:
        return make_response(jsonify({'message': 'Jogador não encontrado'}), 404)
    

@app.route('players/position/<position>', methods = ['GET'])
def get_players_by_position(position):
    cursor = conn.cursor(buffered=True)

    sql = f"SELECT * FROM male_players WHERE Position like '%{position}%';"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    json_data = []
       
    if data:
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)
    else:
        return make_response(jsonify({'message': 'Jogador não encontrado'}), 404)
    

@app.route('/players/club/<club_name>', methods = ['GET'])
def get_players_by_club(club_name):
    cursor = conn.cursor(buffered=True)

    sql = f"SELECT * FROM male_players WHERE Club like '%{club_name}%';"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    json_data = []
       
    if data:
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)
    else:
        return make_response(jsonify({'message': 'Jogador não encontrado'}), 404)
    

@app.route('/players/best', methods = ['GET'])
def get_best_players():
    cursor = conn.cursor(buffered=True)

    sql = f"SELECT * FROM male_players ORDER BY Overall DESC LIMIT 50;"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    data = cursor.fetchall()
    json_data = []
       
    if data:
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)
    else:
        return make_response(jsonify({'message': 'Jogador não encontrado'}), 404)
    

if __name__ == '__main__':
    app.run(debug=True)