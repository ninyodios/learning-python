
def student(name, age):
    print("name:", name)
    print("age:", age)

student("alberto", 42)

# set defaults for arguments
def student_with_defaults(name='unknown', age='999'):
    print("name:", name)
    print("age:", age)

student_with_defaults()
student_with_defaults("afro")

# argument with multiple items
def student_with_multiple_args(name, age, *multiple):
    print("name:", name)
    print("age:", age)
    print("multiple:", multiple)

student_with_multiple_args("alberto", "41", "mates", "ingles")

# argument with multiple items as a K/V
def student_with_multiple_args_kv(name, age, **multiple):
    print("name:", name)
    print("age:", age)
    print(multiple)
    print("notas:")  # prints a dictionary
    for x in multiple:
        print(" -", x)
    for key, value in multiple.items():
        print(key, " ", value)

#student_with_multiple_args_kv('alberto', 41, 'matematicas=8', 'ciencias=7', 'fisica=1')  <-- it will fail!
student_with_multiple_args_kv('alberto', 41, matematicas=8, ciencias=7, fisica=1)   # it works!

