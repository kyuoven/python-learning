pets = [
    'cats',
    'dogs',
]
noises = {
    'cats': 'meow',
    'dogs': 'bark',
}
print(pets)
print(noises)

for pet, noise in noises.items():
    print(f'{pet} does {noise}')
    print('{pet} does {noise}'.format(pet=pet, noise=noise))
