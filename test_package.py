from homework_exercise import some_calculation_function, some_calculation_function2
import numpy as np

def test_some_calculation_function():
    result = some_calculation_function()
    print("fun1:\n", result)
    assert np.all(result == 0)
    assert result.shape == (4, 7)

def test_some_calculation_function2():
    result = some_calculation_function2()
    print("fun2:", result)
    assert result == 18

if __name__ == "__main__":
    test_some_calculation_function()
    test_some_calculation_function2()