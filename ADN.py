from commons.seq import Nucseq
from optparse import OptionParser

class Rosa_ADN(object):
#===============================================================================
#     Problem
# 
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# 
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# 
# Given: A DNA string ss of length at most 1000 nt.
# 
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
# 
# Sample Dataset
# 
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output
# 
# 20 12 17 21
#===============================================================================

    def __init__(self, header = ">h", sequence = "", verbosity = 0):
        self.header = header
        self.sequence = sequence
        self.verobisty = verbosity
    
    def setAttributesFromCmdLine(self):
        self.toolversion="1.0"
        description = "return the respective number of times A C G and T occur in a sequence "
        parser = OptionParser(description=description, version=self.toolversion)
        parser.add_option("-n", "--headerName", dest = "header", action = "store", type = "string", help = "header of the sequence [optional] [format: string]", default = ">h" )
        parser.add_option("-s", "--sequence", dest = "sequence", action = "store", type = "string", help = "sequence [compulsory] [format: string]", default = "" )
        parser.add_option("-v", "--verbosity",    dest = "verbosity",      action = "store",     type = "int",    help = "Verbosity [optional] [default: 0]",                                 default = 0)
        options = parser.parse_args()[0]
        self._setAttributeFromOptions(options)
        
    def _setAttributeFromOptions(self, options):
        self.setInputHeader(options.header)
        self.setInputSequence(options.sequence)
        self.setVerbosity(options.verbosity)
        
    def setInputHeader(self,header):
        self.header = header
        
    def setInputSequence(self,sequence):
        self.sequence = sequence
        
    def setVerbosity(self, verbosity):
        self.verobisty = verbosity
        
    def _checkOptions(self):
        pass
    
    def ADNcount(self):
        iSeq = Nucseq()
        iSeq.setHeader(self.header)
        iSeq.setSequence(self.sequence)
        A = iSeq.countNt("A")
        T = iSeq.countNt("T")
        G = iSeq.countNt("G")
        C = iSeq.countNt("C")
        return("{0} {1} {2} {3}".format(A, C, G, T))
        
    def run(self):
        self._checkOptions()
        self.ADNcount()
        pass



if __name__ == "__main__":
    iRosa_ADN = Rosa_ADN()
    iRosa_ADN.setAttributesFromCmdLine()
    iRosa_ADN.run()    