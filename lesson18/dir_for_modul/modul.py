import task1 as index_

dict_ = {
    'Eugene': 'coder',
    'San': 'beginner coder',
    'Val': 'businessman',
    'Karina': 'doctor'
}
enum_dict = index_.with_index(dict_.values(), start=1)

for x in enum_dict:
    print(x)
