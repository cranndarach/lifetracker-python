import os
import json

while True:
    try:
        with open('usrsettings/settings.json', 'r') as s:
            settings = json.load(s)
        saveloc = settings['saveloc']
        break
    except FileNotFoundError:
        try:
            with open('usrsettings/settings.json', 'w+') as s:
                write_settings = {}
                write_settings['saveloc'] = 'data'
                ws = json.dumps(write_settings)
                s.write(ws)
                settings = json.load(s)
            saveloc = settings['saveloc']
            break
        except FileNotFoundError:
            os.mkdir('usrsettings')
