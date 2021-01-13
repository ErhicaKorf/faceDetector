#%%
pythin_is_cool = True
java_is_cool = False
empty_list = []
secret_value = 3.14

print('Python and Java are both cool: {}'.format(pythin_is_cool and java_is_cool))
print('secret value and python is cool: {}'.format(secret_value and pythin_is_cool))

# %%
statement = False
if statement:
    print('statement is True')

if not statement:
    print('statment is not True')

# %%
if empty_list:
    print('empty list will not evaluate to True')

# %%
val = 3 
if 0 <= val <1 or val ==3:
    print('value is pos or three')

# %%
my_dict = {}

if my_dict:
    print('there is something in my_dict')
else: 
    print('dict is empty')

# %%
greeting = 'hello fellow pythonista'
language = 'Spanish'

if language == 'Spanish':
    greeting = 'Hesjan'

print(greeting)
# %%
