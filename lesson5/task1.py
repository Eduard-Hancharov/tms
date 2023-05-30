dict_1 = {
    # value:key
    'Hello': 1,
    'World': 2
}
print(dict_1)
new_dict = {
    value: key for key, value in dict_1.items()
}
print(new_dict)




hw = dict(Hello=1, World=2)
print(hw)
hw = dict(zip(hw.values(), hw.keys()))
print(hw)