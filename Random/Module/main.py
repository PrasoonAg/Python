#=========================================================================#
# import mymodule # keyword import and the name of the file only
# # this import all the functions of the file
# print(mymodule.generate_Full_Name("Capatain","America"))
# print(mymodule.gravity())
# print(mymodule.person("King"))
# print(mymodule.sum_two_nums(5,4))
#=========================================================================#
# from mymodule import generate_Full_Name, gravity, person
# # specific functions can be imported from file
# print(generate_Full_Name("Steve","Rogers"))
# print(gravity())
# print(person("King"))
# mass = 100
# weight = mass * gravity()
# print(weight)
# print(person('Firstname'))
#=========================================================================#
# from mymodule import generate_Full_Name as fullname, sum_two_nums as total, person as p ,gravity as g
# # during importing we can rename the name of the module
# print(fullname('Asabneh','Yetayeh'))
# print(total(1,9))
# mass = 100
# weight = mass * g()
# print(weight)
# print(p)
# print(p('firstname'))
#=========================================================================#