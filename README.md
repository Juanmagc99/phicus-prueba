# Proyecto Django Tic-Tac-Toe

Este proyecto implementa el backend de un juego de Tic-Tac-Toe (Tres en raya) utilizando Django mediante llamadas rest. Permite jugar a dos jugadores, validar movimientos, visualizar el estado del tablero y comprobar si se ha producido un ganador. También se han implementado algunos tests para verificar la funcionalidad del modelo y las vistas, así como sistema de logs.

Se ha hecho con python 3.12.1

## Instalación

1. Clona este repositorio:

   [git clone https://github.com/Juanmagc99/phicus-prueba.git](https://github.com/Juanmagc99/phicus-prueba.git)
   
   cd tictactoe
   
3. Instala requisitos(se recomienda crear entorno virtual primero):

   pip install -r requirements.txt

4. Aplica la migraciones:

   python manage.py makemigrations
   python manage.py migrate

5. Ejecutar los test:

   python manage.py test
   
5. Inicia la aplicación:

   python manage.py runserver


## Iniciar un Nuevo Juego

- **URL**: `/start_game/`
- **Método**: `GET`
- **Descripción**: Crea un nuevo juego y devuelve el estado inicial del tablero.
- **Ejemplo de Respuesta**:
  
  ```json
  {
      "message": "Game created, you can start as player X or O",
      "game": {
          "id": 1,
          "board": "---------",
          "last_player": "None"
      }
  }

## Hacer un Movimiento

- **URL**: `/play/<int:game_id>/<str:player>/<int:position>/`
- **Método**: `POST`
- **Descripción**: Realiza un movimiento en el tablero.
- **Parámetros**:
  - `game_id`: ID del juego.
  - `player`: Jugador que hace el movimiento (`X` o `O`).
  - `position`: Posición en el tablero (0 a 8).
- **Ejemplo de Respuesta**:
  
  ```json
  {
      "message": "The game must continue the last player was X",
      "game": {
          "id": 1,
          "board": "X--------",
          "last_player": "X"
      }
  }

## Obtener Información del Juego

- **URL**: `/game_info/<int:game_id>/`
- **Método**: `GET`
- **Descripción**: Devuelve el estado actual del juego.
- **Parámetros**:
  - `game_id`: ID del juego.
- **Ejemplo de Respuesta**:
  
  ```json
  {
        "message": "The game must continue the last player was X",
       "game": {
        "id": 1,
        "board": "X--------",
        "last_player": "X"
    }
  }

## Obtener Información del Juego

- **URL**: `/get_all/`
- **Método**: `GET`
- **Descripción**: Devuelve una lista de todos los juegos creados.
- **Ejemplo de Respuesta**:
  
  ```json
  [
    {
        "id": 1,
        "board": "X--------",
        "last_player": "X",
        "is_finished": false,
        "winner": null
    },
    {
        "id": 2,
        "board": "O--------",
        "last_player": "O",
        "is_finished": false,
        "winner": null
    }
]
