from ortools.linear_solver import pywraplp

# Instancia um solver Glop.
solver = pywraplp.Solver.CreateSolver('GLOP')

# Cria as variáveis que terão qualquer valor não-negativo.
x = solver.NumVar(0, 300 , 'a')
u1 = solver.NumVar(0, solver.infinity() , 'u1')
u2 = solver.NumVar(0, solver.infinity() , 'u2')
u3 = solver.NumVar(0, solver.infinity() , 'u3')
u4 = solver.NumVar(0, solver.infinity() , 'u4')

# Equações de restrição:
solver.Add(0.18*u1 + 0.28*u2 + 0.4*u3 + 0.5*u4 <= 0.2125*x)
solver.Add(50*u1 + 70*u2 + 130*u3 + 160*u4 + 2*x <= 15000)
solver.Add(-0.25*u1 - 0.25*u2 + 0.75*u3 + 0.75*u4 >= 0)
solver.Add(0.8*u1 - 0.2*u2 - 0.2*u3 - 0.2*u4 >= 0)
solver.Add(-0.1*u1 + 0.9*u2 - 0.1*u3 - 0.1*u4 >= 0)


# Função objetivo.
solver.Maximize(1000*u1 + 1900*u2 + 2700*u3 + 3400*u4)

# Resolve o sistema.
solver.Solve()

# Mostra os resultados.
print('Solução:')
print('O ganho total será de R$%.2f' % (solver.Objective().Value()))
print('Sendo dividido da seguinte forma:')
print('Andares |  1  |  2  |  3  |  4  ')
print('--------|-----|-----|-----|-----')
print('Unid.   | %d  |  %d |  %d |  %d' % (u1.solution_value(), u2.solution_value(), u3.solution_value(), u4.solution_value()))
print('E destruindo %d construções antigas' % x.solution_value())

