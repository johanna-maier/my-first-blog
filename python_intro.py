def hi(name):
    '''
    Takes in a name, prints individual or generic greeting
        Parameters:
                name (str): A string
    '''
    if name == 'Ola':
        print('Hola ' + name + '!')
    elif name == 'Francesca':
        print('Ciao ' + name + '!')
    elif name == 'Johanna':
        print('Hallo ' + name + '!')
    else:
        print('Hey ' + name + '!')

girls = ['Rachel', 'Johanna', 'Francesca', 'Ola', 'You']

print("test of docstrings")
print(hi.__doc__)
print("end of test of docstrings")

for name in girls:
    hi(name)
    print('Next girl!')

for i in range(1, 6):
    print(i)


print(range(1, 6))

# Create a list of numbers from a range with only the stop argument
my_numbers_list = list(range(5))
print(my_numbers_list)

if 5 > 2:
    print('It works!')
else:
    print('Not true!')

name = 'Johanna'



print(" ")

# Change the volume if it's too loud or too quiet

volume = 101
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
