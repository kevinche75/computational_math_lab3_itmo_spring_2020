import methods
import graphics
try:
    fun = methods.F3([-3, -3, 5])
    i, x, log = methods.comp_bisection_method(-10, 10, fun, 1e-3)
    graphics.draw_bis_method(log, fun, 1e-3)
    i, x, log = methods.comp_fixed_point_method(-10, 10, fun, 1e-3)
    graphics.draw_fix_method(log, fun, 1e-3)
except AssertionError as inst:
    print(inst.args[0])