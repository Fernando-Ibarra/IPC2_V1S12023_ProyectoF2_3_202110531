from flask import Flask, jsonify
from flask import request 

app = Flask(__name__)

@app.route('/getUsers', methods=['GET'])
def getUser():
    try:
        if request.method == 'GET':
            retorno =   [
                            {
                                "usuario": 
                                    [
                                        {
                                            "rol": "cliente",
                                            "nombre": "Juan",
                                            "apellido": "Pérez",
                                            "telefono": "555-1234",
                                            "correo": "juan.perez@example.com",
                                            "contrasena": "contraseña123"
                                        },
                                        {
                                            "rol": "administrador",
                                            "nombre": "María",
                                            "apellido": "Gómez",
                                            "telefono": "555-5678",
                                            "correo": "maria.gomez@example.com",
                                            "contrasena": "password456"
                                        }
                                    ]
                            }
                        ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    

@app.route('/getMovies', methods=['GET'])
def getMovies():
    try:
        if request.method == 'GET':
            retorno =   [ 
                        {
                            "categoria": [
                                {
                                    "nombre": "Drama",
                                    "peliculas": {
                                        "pelicula": [
                                            {
                                                "titulo": "The Departed",
                                                "director": "Martin Scorsese",
                                                "anio": "2006",
                                                "fecha": "2023-06-10",
                                                "hora": "18:45",
                                                "imagen": "https://flxt.tmsimg.com/assets/p162564_p_v8_ag.jpg",
                                                "precio": "50"
                                            },
                                            {
                                                "titulo": "Inception",
                                                "director": "Christopher Nolan",
                                                "anio": "2010",
                                                "fecha": "2023-06-11",
                                                "hora": "20:15",
                                                "imagen": "https://images.mymovies.net/images/film/cin/350x522/fid20452.jpg",
                                                "precio": "55"
                                            },
                                            {
                                                "titulo": "Pulp Fiction",
                                                "director": "Quentin Tarantino",
                                                "anio": "1994",
                                                "fecha": "2023-06-12",
                                                "hora": "19:30",
                                                "imagen": "https://www.miramax.com/assets/Pulp-Fiction1.png",
                                                "precio": "60"
                                            }
                                        ]
                                    }
                                },
                                {
                                    "nombre": "Suspenso",
                                    "peliculas": {
                                        "pelicula": [
                                            {
                                                "titulo": "The Sixth Sense",
                                                "director": "M. Night Shyamalan",
                                                "anio": "1999",
                                                "fecha": "2023-06-10",
                                                "hora": "20:45",
                                                "imagen": "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Sixth_Sense_poster.png",
                                                "precio": "48"
                                            },
                                            {
                                                "titulo": "Gone Girl",
                                                "director": "David Fincher",
                                                "anio": "2014",
                                                "fecha": "2023-06-11",
                                                "hora": "22:00",
                                                "imagen": "https://posterspy.com/wp-content/uploads/2022/08/GoneGirl.jpg",
                                                "precio": "52"
                                            },
                                            {
                                                "titulo": "Shutter Island",
                                                "director": "Martin Scorsese",
                                                "anio": "2010",
                                                "fecha": "2023-06-12",
                                                "hora": "21:15",
                                                "imagen": "https://i.ytimg.com/vi/Udfq0fiScug/movieposter_en.jpg",
                                                "precio": "47"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

@app.route('/getTheaters', methods=['GET'])
def getTheaters():
    try:
        if request.method == 'GET':
            retorno =   [
                            {
                                "cine": 
                                    {
                                        "nombre": "Cine XYZ",
                                        "salas": 
                                            {
                                                "sala": 
                                                    [
                                                        {
                                                            "numero": "#XYZSALA1",
                                                            "asientos": "150"
                                                        },
                                                        {
                                                            "numero": "#XYZSALA2",
                                                            "asientos": "90"
                                                        },
                                                        {
                                                            "numero": "#XYZSALA3",
                                                            "asientos": "110"
                                                        }
                                                    ]
                                            }
                                    }
                            }
                        ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
@app.route('/getCards', methods=['GET'])
def getCards():
    try:
        if request.method == 'GET':
            retorno =   [
                            {
                                "tarjeta": 
                                    [
                                        {
                                            "tipo": "Credito",
                                            "numero": "4567890123456789",
                                            "titular": "Juan",
                                            "fecha_expiracion": "05/2026"
                                        },
                                        {
                                            "tipo": "Debito",
                                            "numero": "9876543210123456",
                                            "titular": "María",
                                            "fecha_expiracion": "11/2023"
                                        }
                                    ]
                            }
                        ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)