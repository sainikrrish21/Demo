#WAP to print this output 
# name - 'Himanshu'
# age - 18
# course - 'AIDS'
#with the help of var length argument
def fun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")
fun(name='Himanshu', age=18 , course='AIDS') 
