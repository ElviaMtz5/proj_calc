import funciones as tf

def test_procesar_multiplica():
  assert tf.multiplica("10","0.5") == 5

def test_procesar_multiplica2():
  assert tf.multiplica("10","1/2") == 5
