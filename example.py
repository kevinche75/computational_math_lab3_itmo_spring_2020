import methods
fun = methods.F3([4, 1, -11])
fun.print_description()
print(methods.bisection_method(-3, 10, fun, 1e-3))
