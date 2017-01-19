import re

DNA_ALPHABET = set(["A", "T", "G", "C", "U", "N"])
##http://www.bioinformatics.org/sms/iupac.html
IUPAC = set(["A", "T", "G", "C", "U", "R", "Y", "S", "W", "K", "M", "B", "D", "H", "V", "N"])
    
class Nucseq(object):
    __slots__ = ("header",  "sequence")
    

    
    ##constructeur : init, eq, ne, repr 
    
    def _init__(self, name = "", sequence = ""):
        self.header = name 
        self.sequence = sequence
        
    def __eq__(self, other):
        if type(self) is type(other) and self.header == other.header and self.sequence == other.sequence :
            return True
        else : 
            return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __repr__(self):
        return "{0} : {1}".format(self.header, self.sequence)
    
    ##set get
    
    def setHeader(self, header):
        self.header= header
    
    
    def getHeader(self):
        return self.header
    
    def setSequence(self, sequence):
        self.sequence = sequence
        
    def getSequence(self):
        return self.sequence
    
    
    def seqClean(self):
        cleanSeq = ""
        for i in range(0,len(self.sequence),1):
            if self.sequence[i] in IUPAC:
                cleanSeq += self.sequence[i]
            elif self.sequence[i] == "-":
                pass
            else : 
                print("warning : {0} symbol is not known in IUPAC nucleotidic sequences (sequence {1} ; position {2}) ".format(self.sequence[i], self.header, i))
                cleanSeq += "N"
            
        self.setSequence(cleanSeq)
        
    def upCase(self):
        self.setSequence(self.sequence.upper())
        
    def lowCase(self):
        self.setSequence(self.sequence.lower())
        
    def countNt(self,nt):
        return self.sequence.count(nt)
    
        
    def getLength(self, countN= True):
        if countN :
            return len(self.sequence)
        else : 
            return len(self.sequence)-self.countNt("N")
    
    def translation(self,):
        self.setSequence(re.sub("T","U",self.sequence))