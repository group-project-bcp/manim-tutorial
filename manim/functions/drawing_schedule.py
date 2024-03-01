from function import Function
from quadratic_function import QuadraticFunction
from homographic_function import HomographicFunction
from manim import *

linear_functions_1 = [
    Function("f(x) = 2x", lambda x: np.array([x, 2*x, 0])),
    Function("f(x) = 3x", lambda x: np.array([x, 3*x, 0])),
    Function("f(x) = 1/2x", lambda x: np.array([x, 1/2*x, 0])),
    Function("f(x) = 1/4x", lambda x: np.array([x, 1/4*x, 0])),
    Function("f(x) = 1/8x", lambda x: np.array([x, 1/8*x, 0])),
    Function("f(x) = -x", lambda x: np.array([x, -x, 0])),
    Function("f(x) = -2x", lambda x: np.array([x, -2*x, 0])),
    Function("f(x) = -3x", lambda x: np.array([x, -3*x, 0])),
    Function("f(x) = -1/2x", lambda x: np.array([x, -1/2*x, 0])),
    Function("f(x) = -1/4x", lambda x: np.array([x, -1/4*x, 0])),
    Function("f(x) = -1/8x", lambda x: np.array([x, -1/8*x, 0])),
]

linear_functions_2 = [   
    Function("f(x) = x", lambda x: np.array([x, x, 0])),
    Function("f(x) = x + 1", lambda x: np.array([x, x + 1, 0])),
    Function("f(x) = x + 2", lambda x: np.array([x, x + 2, 0])),
    Function("f(x) = x - 1", lambda x: np.array([x, x - 1, 0])),
    Function("f(x) = x - 2", lambda x: np.array([x, x - 2, 0])),
    Function("f(x) = 2x - 3", lambda x: np.array([x, 2*x - 3, 0])),
    Function("f(x) = -x + 1", lambda x: np.array([x, -x + 1, 0])),
    Function("f(x) = -x + 2", lambda x: np.array([x, -x + 2, 0])),
    Function("f(x) = -x - 1", lambda x: np.array([x, -x - 1, 0])),
    Function("f(x) = -x - 2", lambda x: np.array([x, -x - 2, 0])),
]


quadratic_functions_1 = [    
    Function("f(x) = x^2", lambda x: np.array([x, x**2, 0])),
    Function("f(x) = -x^2", lambda x: np.array([x, -x**2, 0])),
]

quadratic_functions_2 = [
    QuadraticFunction("f(x) = x^2 + 1", (0, 1)),
    QuadraticFunction("f(x) = x^2 + 2", (0, 2)),
    QuadraticFunction("f(x) = x^2 - 1", (0, -1)),
    QuadraticFunction("f(x) = x^2 - 2", (0, -2)),
    QuadraticFunction("f(x) = (x - 1)^2", (1, 0)),
    QuadraticFunction("f(x) = (x - 1)^2 + 2", (1, 2)),
]

homographic_functions = [
    HomographicFunction(1, (0, 0)),
    HomographicFunction(1, (2, 0)),
    HomographicFunction(2, (-1, 1)),
]