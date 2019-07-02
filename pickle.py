#!/usr/bin/env python3
import pickle
# начать с любого инстанса типа Python
original = { 'a': 0, 'b': [1, 2, 3] }
# преобразовать это в строку
pickled = pickle.dumps(original)
# преобразовать обратно в идентичный объект
identical = pickle.loads(pickled)
