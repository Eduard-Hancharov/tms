Parent1 = type('Parent1', (), {'a': 'value_a'})
Parent2 = type('Parent2', (), {'b': 'value_b'})
class Child(Parent1, Parent2):
    c = 'value_c'