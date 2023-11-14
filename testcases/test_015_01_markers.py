import pytest


class Test_15_marker():

    @pytest.mark.skip
    def test_add(self):
        a = 10
        b=5
        add = a+b
        if(add == 15):
            print("\n ******* ADDITION IS SUCESSFUL ********")
            print("ADDTION=",add)
            assert True
        else:
            print("\n *********** INVALID OPERATION *******")
            assert False


    @pytest.mark.skipif
    def test_sub(self):
        a = 10
        b =5
        sub =a-b
        if(sub == 5):
            print("\n********** SUBSTRACTION IS SUCESSFUL *********")
            print("substraction=",sub)
            assert True
        else:
            print("********* INVALID OPERATION **********")

    @pytest.mark.xfail
    def test_mul(self):
        a =10
        b=5
        mul=a*b
        if(mul == 50):
            print("\n ******** MULTIPLICATION IS SUCESSFUL *********")
            print("multiplication=",mul)
            assert True
        else:
            print("\n ***** INVALID OPERATION *******")
            assert False

    def test_div(self):
        a=10
        b=5
        div=a/b
        if(div == 2):
            print("\n ******* DIVISION IS OPERATION ********")
            print("division=",div)
            assert True
        else:
            print("\n ********* INVALID OPERATION ********")
            assert False

