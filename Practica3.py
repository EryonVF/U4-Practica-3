from flask import Flask, request, jsonify, json  


app = Flask(__name__)


# Inicializamos un diccionario vacío
diccionario = {}


# 1-.Obtener diccionario 
# 1.http://localhost:5000/get_diccionario
@app.route('/get_diccionario', methods=['GET'])
def get_diccionario():
    return jsonify(diccionario)


# 2-.Agregar una clave-valor al diccionario
#2.http://localhost:5000/agregar_clave_valor/edad/21
@app.route('/agregar_clave_valor/<string:clave>/<string:valor>', methods=['GET'])
def agregar_clave_valor_route(clave, valor):
    diccionario[clave] = valor
    return jsonify(diccionario)


# 3-.Ruta para eliminar una clave del diccionario
#3.http://localhost:5000/eliminar_clave/edad
@app.route('/eliminar_clave/<string:clave>', methods=['GET'])
def eliminar_clave(clave):
    if clave in diccionario:
        del diccionario[clave]
        return jsonify(diccionario)
    else:
        return 'La clave no existe en el diccionario', 404


# 4-.Ruta para modificar el valor de una clave en el diccionario
# 4.http://localhost:5000/modificar_valor/edad/22
@app.route('/modificar_valor/<string:clave>/<string:nuevo_valor>', methods=['GET'])
def modificar_valor(clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return jsonify(diccionario)
    else:
        return 'La clave no existe en el diccionario', 404


# 5-.Combinar dos diccionarios mediante parámetros de consulta
# 5.http://localhost:5000/combinar_diccionarios?diccionario2={"eryon":"velasco"}
@app.route('/combinar_diccionarios', methods=['GET'])
def combinar_diccionarios():
    diccionario2_str = request.args.get('diccionario2')
    if not diccionario2_str:
        return 'Parámetro "diccionario2" no proporcionado en la URL', 400

    try:
        diccionario2 = eval(diccionario2_str)
        if not isinstance(diccionario2, dict):
            raise ValueError()
    except (SyntaxError, ValueError):
        return 'El parámetro "diccionario2" no es un diccionario válido', 400

    diccionario.update(diccionario2)
    return jsonify(diccionario)


# 6-.Agregar un elemento a un conjunto
# 6.http://localhost:5000/agregar_elemento_conjunto/nuevo_elemento?conjunto=["Primer_elemento", "Segundo_Elemento"]
@app.route('/agregar_elemento_conjunto/<string:elemento>', methods=['GET'])
def agregar_elemento_conjunto(elemento):
    if 'conjunto' not in request.args:
        request.args['conjunto'] = '[]'
    conjunto = set(json.loads(request.args['conjunto']))
    conjunto.add(elemento)
    return jsonify(list(conjunto))


# 7-.Eliminar un elemento de un conjunto
# 7.http://localhost:5000/eliminar_elemento_conjunto/elemento_a_eliminar?conjunto=["Primer_elemento", "Segundo_Elemento", "elemento_a_eliminar"]
@app.route('/eliminar_elemento_conjunto/<string:elemento>', methods=['GET'])
def eliminar_elemento_conjunto(elemento):
    if 'conjunto' not in request.args:
        request.args['conjunto'] = '[]'
    conjunto = set(json.loads(request.args['conjunto']))
    if elemento in conjunto:
        conjunto.remove(elemento)
        return jsonify(list(conjunto))
    else:
        return 'El elemento no existe en el conjunto', 404


# 8-.Combinar dos conjuntos
# 8.http://localhost:5000/combinar_conjuntos?conjunto1=["Primer_elemento",%20"Segundo_Elemento"]&conjunto2=["Tercer_Elemento",%20"Cuarto_Elemento"]
@app.route('/combinar_conjuntos', methods=['GET'])
def combinar_conjuntos():
    if 'conjunto1' not in request.args:
        request.args['conjunto1'] = '[]'
    if 'conjunto2' not in request.args:
        request.args['conjunto2'] = '[]'
    conjunto1 = set(json.loads(request.args['conjunto1']))
    conjunto2 = set(json.loads(request.args['conjunto2']))
    conjunto_resultante = conjunto1.union(conjunto2)
    return jsonify(list(conjunto_resultante))


# 9-.Obtiene la diferencia entre dos conjuntos
# 9.http://localhost:5000/diferencia_entre_conjuntos?conjunto1=["Primer_elemento", "Segundo_Elemento", "Tercer_Elemento"]&conjunto2=["Segundo_Elemento", "Tercer_Elemento", "Cuarto_Elemento"]
@app.route('/diferencia_entre_conjuntos', methods=['GET'])
def diferencia_entre_conjuntos():
    if 'conjunto1' not in request.args:
        request.args['conjunto1'] = '[]'
    if 'conjunto2' not in request.args:
        request.args['conjunto2'] = '[]'
    conjunto1 = set(json.loads(request.args['conjunto1']))
    conjunto2 = set(json.loads(request.args['conjunto2']))
    diferencia = conjunto1.difference(conjunto2)
    return jsonify(list(diferencia))


# 10-.Agrega un elemento a una tupla y crear una nueva tupla
# 10.http://localhost:5000/agregar_elemento_tupla/5/[1, 2, 3, 4]
@app.route('/agregar_elemento_tupla/<string:elemento>/<tupla>', methods=['GET'])
def agregar_elemento_tupla(elemento, tupla):
    tupla_list = json.loads(tupla)
    tupla_list.append(elemento)
    nueva_tupla = tuple(tupla_list)
    return jsonify(list(nueva_tupla))


# 11-.Elimina un elemento de una tupla y crear una nueva tupla
# 11.http://localhost:5000/eliminar_elemento_tupla/elemento_a_eliminar?tupla=(1,2,3,4)
@app.route('/eliminar_elemento_tupla/<string:elemento>', methods=['GET'])
def eliminar_elemento_tupla(elemento):
    if 'tupla' not in request.args:
        return 'La tupla no se proporcionó en la URL', 400

    tupla_str = request.args['tupla']
    tupla = eval(tupla_str)  # Analiza la cadena para obtener la tupla
    nueva_tupla = tuple(e for e in tupla if e != elemento)
    return jsonify(list(nueva_tupla))


# 12-.Concatenar dos tuplas 
# 12.http://localhost:5000/concatenar_tuplas?tupla1=[6,5,4]&tupla2=[3,2,1]
@app.route('/concatenar_tuplas', methods=['GET'])
def concatenar_tuplas():
    if 'tupla1' not in request.args:
        return 'La tupla1 no se proporcionó en la URL', 400
    if 'tupla2' not in request.args:
        return 'La tupla2 no se proporcionó en la URL', 400

    tupla1_str = request.args['tupla1']
    tupla2_str = request.args['tupla2']

    tupla1 = tuple(json.loads(tupla1_str))
    tupla2 = tuple(json.loads(tupla2_str))

    nueva_tupla = tupla1 + tupla2
    return jsonify(list(nueva_tupla))

# 13-.Revertir el orden de una tupla y crear una nueva tupla
# http://localhost:5000/revertir_tupla?tupla=[1,2,3,4]
@app.route('/revertir_tupla', methods=['GET'])
def revertir_tupla():
    if 'tupla' not in request.args:
        request.args['tupla'] = '[]'
    tupla = tuple(json.loads(request.args['tupla']))
    nueva_tupla = tuple(reversed(tupla))
    return jsonify(list(nueva_tupla))

if __name__ == "__main__":
    app.run()

