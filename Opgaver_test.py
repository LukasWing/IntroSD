import os
import unittest
import math
from Opgaver import *

class TestScience(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(foo(), "foo")

    def test_bar(self):
        self.assertEqual(bar(3),"Bar 3.")
        self.assertEqual(bar(123241234132),"Bar 123241234132.")

    def test_getPositives(self):
        input = [1, -3, 4]
        expected = [1, 4]
        self.assertEqual(getPositives(input), expected)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(0, 4), 0)
        self.assertEqual(multiply(1.5, 2.5), 3.75)
    
    def test_divide(self):
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(2, -3), -0.6666666666666666)
        self.assertEqual(divide(0, 4), 0)
        self.assertEqual(divide(1.5, 2.5), 0.6)
        # self.assertEqual(divide(1, 0), "Error")

    def test_concatenate(self):
        self.assertEqual(concatenate("Hello", "World", "!"), "HelloWorld!")
        self.assertEqual(concatenate("Hello", "World", " "), "Hello World ")
        self.assertEqual(concatenate("Hello", " ", "There"), "Hello There")

    def test_isFirstSameAsLast(self):
        self.assertEqual(isFirstSameAsLast("VG"), False)
        self.assertEqual(isFirstSameAsLast("VGV"), True)
        self.assertEqual(isFirstSameAsLast("abcde"), False)
        self.assertEqual(isFirstSameAsLast("abadlfnknfkaj.dfngljdb,rghjddfhjbghj,dbghj,dsaa#%¤#cba"), True)
        self.assertEqual(isFirstSameAsLast("a"), True)

    def test_isNumber(self):
        self.assertEqual(isNumber(1), True)
        self.assertEqual(isNumber("1.5.5"), False)
        self.assertEqual(isNumber("1"), False)
        self.assertEqual(isNumber(0.1), True)

    def test_isEven(self):
        self.assertEqual(isEven(1), False)
        self.assertEqual(isEven(2), True)
        self.assertEqual(isEven(0), True)
        self.assertEqual(isEven(0.1), False)

    def test_isOdd(self):
        self.assertEqual(isOdd(1), True)
        self.assertEqual(isOdd(2), False)
        self.assertEqual(isOdd(0), False)
        self.assertEqual(isOdd(0.1), False)
    
    def test_containsLukas(self):
        self.assertEqual(containsLukas("Lukas"), True)
        self.assertEqual(containsLukas("Lukas "), True)
        self.assertEqual(containsLukas("Lucas "), False)
        self.assertEqual(containsLukas("Lukas is a cool guy"), True)
        self.assertEqual(containsLukas("!"), False)   

    def test_discriminant(self):
        self.assertEqual(discriminant(1, 2, 3), -8)
        self.assertEqual(discriminant(1, 0, 0), 0)
        self.assertEqual(discriminant(1, 2, 1), 0)
        self.assertEqual(discriminant(1, 2, 0), 4)

    def test_makeRoster(self):
        self.assertEqual(makeRoster("John", "Jane", "Mathias"), ["John", "Jane", "Mathias"])
        self.assertEqual(makeRoster("William", "Lukas", "Mathias"), ["William", "Lukas", "Mathias"])
    
    def test_addNameToRoster(self):
        self.assertEqual(addNameToRoster(["Jane", "Mathias"], "John"), ["Jane", "Mathias", "John"])
        self.assertEqual(addNameToRoster(["Lukas", "Mathias"], "William"), ["Lukas", "Mathias", "William"])
        self.assertEqual(addNameToRoster([], "William"), ["William"])

    def test_isNameOnRoster(self):
        self.assertEqual(isNameOnRoster(["John", "Jane", "Mathias"], "John"), True)
        self.assertEqual(isNameOnRoster(["John", "Jane", "Mathias"], "Jane"), True)
        self.assertEqual(isNameOnRoster(["John", "Jane", "Mathias"], "Mathias"), True)
        self.assertEqual(isNameOnRoster(["John", "Jane", "Mathias"], "William"), False)
        self.assertEqual(isNameOnRoster(["John", "Jane", "Mathias"], "Lukas"), False)
    
    def test_canIAffordIt(self):
        self.assertEqual(canIAffordIt([1, 3], 6), True)
        self.assertEqual(canIAffordIt([1, 2, 3], 7), True)
        self.assertEqual(canIAffordIt([1, 2, 3], 5), False)
        self.assertEqual(canIAffordIt([1, 2, 3], 4), False)
        self.assertEqual(canIAffordIt([3, 3, 3], 9), True)

    def test_Q(self):
        inputM = 1
        inputL_f = 334
        expected = 334
        self.assertAlmostEqual(Q(inputM,inputL_f),expected)
        inputM = 3.5
        inputL_f = 25000
        expected = 87500
        self.assertAlmostEqual(Q(inputM,inputL_f),expected)
        inputM = math.sqrt(7)
        inputL_f = 207000
        expected = 547670.52
        self.assertAlmostEqual(Q(inputM,inputL_f),expected,1)
        inputM = -1
        inputL_f = 334
        expected = -1
        self.assertAlmostEqual(Q(inputM,inputL_f),expected)
    
    def test_kineticEnergy(self):
        self.assertAlmostEqual(kineticEnergy(2,4), 16)
        self.assertAlmostEqual(kineticEnergy(1,6), 18)

    def test_molarmass(self):
        self.assertAlmostEqual(molarmass(2,1), 2)
        self.assertAlmostEqual(molarmass(1,2), 0.5)
        self.assertAlmostEqual(molarmass(1,1), 1)
        self.assertAlmostEqual(molarmass(2,2), 1)

