import pytest


class Test_015_02_userdefined_marker():

    @pytest.mark.customer
    def test_add_cust(self):
        print("\n ****** CUSTOMER ADDED SUCESSFULLY ********")

    @pytest.mark.customer
    def test_add_cust(self):
        print("\n ******** CUSTOMEER DELETED SUCESSFULLY *******")

    @pytest.mark.product
    def test_add_product(self):
        print("\n ******* PRODUCT ADDED SUCSSFULLY ***********")

    @pytest.mark.customer
    def test_del_product(self):
        print("\n ********* PRODUCT DELETED SUCESSFULLY *******")

    @pytest.mark.bill
    def test_add_bill(self):
        print('\n******BILL ADDED SUCCESSFULLY*****')

    @pytest.mark.bill
    def test_del_bill(self):
        print('\n*****BILL DELETD SUCCESSFULLY*****')

    @pytest.mark.sanity
    @pytest.mark.patient
    def test_add_patient(self):
        print("\n ****** PATIENT ADMITTED SUCESSFULLY *********")

    @pytest.mark.regression
    @pytest.mark.patient
    def test_dis_patient(self):
        print('\n*****PATIENT DISCHARGED SUCCESSFULLY*****')
