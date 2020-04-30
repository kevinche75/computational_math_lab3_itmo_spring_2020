import methods
import graphics

try:
    fun = methods.F1(2, [-3, -4, 1])
    i, x, log = methods.comp_bisection_method(-3, 10, fun, 1e-3)
    graphics.draw_bis_method(log, fun, 1e-3)
    i, x, log = methods.comp_fixed_point_method(-3, 10, fun, 1e-3)
    graphics.draw_fix_method(log, fun, 1e-3)
except AssertionError as inst:
    print(inst.args[0])

# f1 = methods.F5([0.1, 1, 0, 0, 0.2, -0.3,0,0,0,0])
# f2 = methods.F5([0.2, 0, -0.1, 1, 0, -0.7,0,0,0,0])
# f3 = methods.F5([1, 0, 3, -2, 1, 3, 0,0,0,0])
# vector_x, log = methods.newtons_method([0.25, 0.75, 1], [f1, f2, f3], 1e-2)
# graphics.draw_newton_method_4d(log, [f1,f2, f3], 1e-2)
# 0.1x^2 + 1.0x + 0.0xy + 0.0y + 0.2y^2 + -0.3yz + 0.0z + 0.0z^2 + 0.0zx + 0.0 = 0
# 0.2x^2 + 0.0x + -0.1xy + 1.0y + 0.0y^2 + -0.7yz + 0.0z + 2.0z^2 + 1.0zx + 0.0 = 0
# 1.0x^2 + 0.0x + 3.0xy + -2.0y + 1.0y^2 + 3.0yz + 0.3z + 0.2z^2 + 1.0zx + 0.0 = 0

# solve.solve_set()