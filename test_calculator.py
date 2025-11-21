import pytest
import pandas as pd
from calculator import Calculator  # 待实现的模块

# 读取测试用例
test_data = pd.read_csv("test_cases.csv").to_dict('records')


@pytest.mark.parametrize("case", test_data)
def test_calculator(case):
    calc = Calculator()
    op = case["operation"]
    a, b = case["a"], case["b"]
    expected = case["expected_result"]

    if op == "add":
        result = calc.add(a, b)
    elif op == "subtract":
        result = calc.subtract(a, b)
    elif op == "multiply":
        result = calc.multiply(a, b)
    elif op == "divide":
        result = calc.divide(a, b)
    else:  # invalid
        with pytest.raises(ValueError, match="Invalid input"):
            if isinstance(a, str):
                calc.add(a, b)
            else:
                calc.add(a, b)  # 强制触发异常
        return

    assert str(result) == str(expected), f"{op}({a}, {b}) expected {expected}, got {result}"
