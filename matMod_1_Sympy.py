import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)

diffEq1 = sp.Eq(y * (1 + sp.ln(y)) + 2 * x * sp.diff(y, x), 0)
diffEq2 = sp.Eq(x * sp.diff(y, x), x + 5*y + (4*y**2) / x)
diffEq3 = sp.Eq(sp.diff(y, x) + 2*x*y, x)

solution1 = sp.dsolve(diffEq1, y)

#depending on the hint there are a few different solution
solution2 = sp.dsolve(diffEq2, y, hint="1st_homogeneous_coeff_subs_dep_div_indep")

#initial state y(1) = 2
solution3 = sp.dsolve(diffEq3, y, ics={y.subs(x, 1): 2})

print(solution1)
print(solution2)
print(solution3)