from mendeleev.fetch import fetch_table
ptable = fetch_table('elements')
def numero_atomico(simbolo):
  num_at = ptable[ptable.symbol==simbolo]['atomic_number'].to_list()[0]
  return num_at

def simbolo_atomico(simbolo):
  sim_at = ptable[ptable.symbol==simbolo]['symbol'].to_list()[0]
  return sim_at

def peso_atomico(simbolo):
  peso_at = ptable[ptable.symbol==simbolo]['atomic_weight'].to_list()[0]
  return peso_at

def conf_electronica(simbolo):
  conf_el = ptable[ptable.symbol==simbolo]['electronic_configuration'].to_list()[0]
  return conf_el

conf_electronica.__doc__ = '''
Regresa la configuracion electronica del elemento
Uso: conf_electronica(string)
'''

def info_elemento(simbolo):
  print('Numero Atomico = '+ str(numero_atomico(simbolo)))
  print('Simbolo = '+simbolo_atomico(simbolo))
  print('Peso atomico = ' + str(peso_atomico(simbolo)))
  print('Configuracion electronica = '+conf_electronica(simbolo))

info_elemento.__doc__ = '''
Funcion para escribir informacion sobre un elemento quimico.
Regresa
-Numero atomico
-Simbolo
-Peso atomico
-Configuracion electronica

'''
