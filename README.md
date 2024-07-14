# Proyecto Django Tic-Tac-Toe

Este proyecto implementa el backend de un juego de Tic-Tac-Toe (Tres en raya) utilizando Django. Permite jugar a dos jugadores, validar movimientos, visualizar el estado del tablero y comprobar si se ha producido un ganador. También se han implementado algunos tests para verificar la funcionalidad del modelo y las vistas.

Se ha hecho con python 3.12.1

## Instalación

1. Clona este repositorio:

   [git clone https://github.com/tu-usuario/tic-tac-toe-django.git](https://github.com/Juanmagc99/phicus-prueba.git)
   cd tictactoe
   
2. Instala requisitos(se recomienda crear entorno virtual primero):

   pip install -r requirements.txt

3. Aplica la migraciones:

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

