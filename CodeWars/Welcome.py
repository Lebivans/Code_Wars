'''
https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python
'''

def greet(language):
  if language=='english':
    return('Welcome')
  elif language=='czech':
    return('Vitejte')
  elif language=='danish':
    return('Velkomst')
  elif language=='dutch':
    return ('Welkom')
  elif language=='estonian':
    return('Tere tulemast')
  elif language=='finnish':
    return('Tervetuloa')
  elif language=='flemish':
    return('Welgekomen')
  elif language=='french':
    return('Bienvenue')
  elif language=='german':
    return('Willkommen')
  elif language=='irish':
    return('Failte')
  elif language=='italian':
    return('Benvenuto')
  elif language=='latvian':
    return ('Gaidits')
  elif language=='lithuanian':
    return ('Laukiamas')
  elif language=='polish':
    return ('Witamy')
  elif language=='spanish':
    return('Bienvenido')
  elif language=='swedish':
    return('Valkommen')
  elif language=='welsh':
    return('Croeso')
  else:
    return('Welcome')

# Более рациональный вариант решения этой задачи

def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')