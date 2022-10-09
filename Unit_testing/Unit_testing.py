import unittest

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP Called...")
        self.a=10
        self.b=20
        
    def teardown(self):
        self.a=0
        self.b=0
        print("TEARDOWN Called...")
        
    def test_sumfunc_1(self):
        print("TEST-1 Called...")
        #Act
        result=sum(self.a,self.b)
        #Assert
        self.assertEqual(result,self.a+self.b)
    
    def test_sumfunc_2(self):
        print("TEST-2 Called...")
        #Act
        result=sum(self.a,self.b)
        #Assert
        self.assertEqual(result,self.a+self.b)
        
if __name__=="__main__":
    unittest.main()

