# coding:utf-8
import pytest

@pytest.mark.parametrize("test_input,expected",
                        [ ("1+2",3),
                          ("3+4",7),
                          ("6*9",56),
                         ])

def test_eval(test_input,expected):
    assert eval(test_input)==expected

if __name__ == "__main__":
    pytest.main(["s","test_canshu1.py"])