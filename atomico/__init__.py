from mendeleev.fetch import fetch_table
ptable = fetch_table('elements')
def numero_atomico(simbolo):
  '''
  regresa el numero atomico.
  Uso: num_at(string) 
  string -> simbolo, eg. 'H','K','Be'
  '''
  num_at = ptable[ptable.symbol==simbolo]['atomic_number'].to_list()[0]
  return num_at

def simbolo_atomico(simbolo):
  '''
  Regresa el simbolo atomico.
  Uso: simbolo_atomico(string)
  string -> simbolo, eg. 'H','K','Be'
  '''
  sim_at = ptable[ptable.symbol==simbolo]['symbol'].to_list()[0]
  return sim_at

def peso_atomico(simbolo):
  '''
  Regresa el peso atomico.
  Uso: peso_atomico(string)
  string -> simbolo, eg. 'H','K','Be'
  '''
  peso_at = ptable[ptable.symbol==simbolo]['atomic_weight'].to_list()[0]
  return peso_at

def conf_electronica(simbolo):
  '''
  Regresa la configuracion electronica del elemento
  Uso: conf_electronica(string)
  string -> simbolo, eg. 'H','K','Be'
  '''

  conf_el = ptable[ptable.symbol==simbolo]['electronic_configuration'].to_list()[0]
  return conf_el

conf_electronica.__doc__ = 

def info_elemento(simbolo):
  '''
  Funcion para escribir informacion sobre un elemento quimico.
  Regresa
  -Numero atomico
  -Simbolo
  -Peso atomico
  -Configuracion electronica
  Uso: info_elemento(string)
  string -> simbolo, eg. 'H','K','Be'
'''
  print('Numero Atomico = '+ str(numero_atomico(simbolo)))
  print('Simbolo = '+simbolo_atomico(simbolo))
  print('Peso atomico = ' + str(peso_atomico(simbolo)))
  print('Configuracion electronica = '+conf_electronica(simbolo))


