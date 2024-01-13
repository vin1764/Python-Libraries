def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

#We use args and kwargs to pass in parameters when we dont know how many parameters
#we would haave to pass.Eg:

student_info('Mayank','Maya',age='18',subject='Math')

#args represent positinal arguments.They will be returned directly in the given order in form
#of a tuple.

#KWARGS represent keyword arguments. They are returned with the category(keyword) mentioned first
#and then the corresponding data, in the form of a dictionary

#POSITIONAL ARGUMENTS always precede KEYWORD ARGUMENTS in a call
