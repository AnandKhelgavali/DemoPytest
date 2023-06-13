import pytest

class Test_py03:
    @pytest.mark.group3
    def test_sum_006(self):
        a = 8
        b = 8
        sum = a + b
        print("sum -- >" + str(sum))
        if sum == 16:
            assert True
        else:
            assert False
