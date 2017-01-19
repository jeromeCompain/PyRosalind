from commons.seq import Nucseq

h=">setters"
seq="ATGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
print("{0}".format(iSeq))

h=">seqClean_alphabetADN"
seq="ATGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.seqClean()
print("{0}".format(iSeq))

h=">seqClean_alphabetARN"
seq="AUGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.seqClean()
print("{0}".format(iSeq))

h=">seqClean_IUPAC"
seq="ATGCURYSWKMBDHVN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.seqClean()
print("{0}".format(iSeq))

h=">seqClean_IUPAC_cleaningdata"
seq="ATGCU-RYSWK-MBDHV-N"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.seqClean()
print("{0}".format(iSeq))

h=">seqClean_IUPAC_missingdata"
seq="ATGCE"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.seqClean()
print("{0}".format(iSeq))

h=">lowercase"
seq="ATGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.lowCase()
print("{0}".format(iSeq))

h=">uppercase"
seq="atgcn"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.upCase()
print("{0}".format(iSeq))

h=">countNt"
seq="ATATTGCGTAATGCCAGTATGGCCCAGTAGCAACCAGT"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
A = iSeq.countNt("A")
T = iSeq.countNt("T")
G = iSeq.countNt("G")
C = iSeq.countNt("C")
print("{0} {1} {2} {3}".format(A, T, G, C))

h=">lengthwN"
seq="ATGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
length = iSeq.getLength()
print("{0}".format(length))

h=">lengthwoN"
seq="ATGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
length = iSeq.getLength(False)
print("{0}".format(length))


h=">translation"
seq="ATGCN"

iSeq = Nucseq()
iSeq.setHeader(h)
iSeq.setSequence(seq)
iSeq.translation()
print("{0}".format(iSeq))
