def add_binary(a,b):
    return bin(sum([a,b])).split('b')[-1]
    
    
Test.assert_equals(add_binary(1,1),"10")
Test.assert_equals(add_binary(0,1),"1")
Test.assert_equals(add_binary(1,0),"1")
Test.assert_equals(add_binary(2,2),"100")
Test.assert_equals(add_binary(51,12),"111111")
