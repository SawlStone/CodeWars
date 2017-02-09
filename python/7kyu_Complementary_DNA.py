def DNA_strand(dna):
    return dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    
    
    
# Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
