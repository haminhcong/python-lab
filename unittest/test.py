import os
import unittest
import tempfile


class BankAccount:
    def __init__(self,init_balance):
        if init_balance <= 1000:
            raise ValueError('initial balance must be > 1000')
        self.balance = init_balance

    def deposit(self,amount):
        if amount <= 1:
            return "error"
        else:
            self.balance+=amount
            return "success"

    def withdraw(self,amount):
        self.balance -= amount
        return "success"

    def check_balance(self):
        return self.balance


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_1(self):
        a = BankAccount(5000)
        result = a.withdraw(3000)
        assert 'success' in result

    def test_case_2(self):
        with self.assertRaises(ValueError) as context:
            a = BankAccount(-5000)
        self.assertTrue('initial balance must be > 1000' in context.exception)

    def test_case_3(self):
        a = BankAccount(5000)
        result = a.deposit(-3000)
        assert 'error' in result

    def test_case_4(self):
        a = BankAccount(5000)
        result = a.withdraw(8000)
        assert 'error' in result

if __name__ == '__main__':
    unittest.main()


