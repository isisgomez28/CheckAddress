"""
This script runs the CheckAddress application using a development server.
"""

from os import environ
from CheckAddress import app

"""
    Configs
"""
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
SECRET_KEY = 'Hello Flask CheckAddress'

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.config['SECRET_KEY'] = 'Hello Flask CheckAddress'
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'public'
    app.config['RECAPTCHA_PRIVATE_KEY'] = 'private'
    app.run(HOST, PORT)
