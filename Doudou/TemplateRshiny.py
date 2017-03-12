from optparse import OptionParser

class Template_Rshiny(object):
#===============================================================================
#
#===============================================================================

    def __init__(self, filename = "", verbosity = 0):
        self.filename = filename
        self.verbosity = verbosity 
    
    def setAttributesFromCmdLine(self):
        self.toolversion="1.0"
        description = ""
        parser = OptionParser(description=description, version=self.toolversion)
#        parser.add_option("-n", "--headerName", dest = "header", action = "store", type = "string", help = "header of the sequence [optional] [format: string]", default = ">h" )
        parser.add_option("-f", "--filename", dest = "filename", action = "store", type = "string", help = "filename [compulsory] [format: string]", default = "sahdcalib.txt" )
        parser.add_option("-v", "--verbosity",    dest = "verbosity",      action = "store",     type = "int",    help = "Verbosity [optional] [default: 0]", default = 0)
        options = parser.parse_args()[0]
        self._setAttributeFromOptions(options)
        
    def _setAttributeFromOptions(self, options):
        self.setInputFilename(options.filename)
        self.setVerbosity(options.verbosity)
        
    def setInputFilename(self,filename):
        self._filename = filename
        self.setOutputFilename(filename)
        self.setRscriptFilename(filename)
        
    def setOutputFilename(self,filename):
        self._outname = "{0}.out".format(filename)
        
    def setRscriptFilename(self,filename):
        self._Rscript = "{0}.R".format(filename)

        
    def setVerbosity(self, verbosity):
        self.verbosity = verbosity
        
    def _checkOptions(self):
        pass
    
    def fileParser(self):
        with open(self._filename, "r") as f:
            line = f.readline()
            lVariables = line.rstrip().split("\t")
            self.lVariables = []
            for var in lVariables:
                self.lVariables.append(var.replace("\"", ""))
            output = open(self._outname, "w")
            output.write(line.replace("\"", ""))
            
            line = f.readline()
            while line :
                outLine = self.lineParser(line)
                output.write(outLine)
                line = f.readline()
            output.close()
            f.close()
        
        
        
        
        
    def lineParser(self, line):
        outLine = ""
        lValues = line.rstrip().split("\t")
        dValues = {}
        
        for i,var in enumerate(self.lVariables) :
            dValues[var] = lValues[i+1] ## decalage parce que le fichier a une premiere colonne en trop
        
        ### supprimer des caracteres en trop ; verifier que les modalites son connues
        tmp = dValues["famhist"]
        dValues["famhist"] = tmp.replace("\"", "")
        if dValues["famhist"] != "Absent" and dValues["famhist"] != "Present":
            print("probleme a la ligne {0} : modalite inconnue".format(dValues["row.names"]))
            
        ### controler que des variables quanti sont dans un espace "normal"
        dValues["sbp"] = int(dValues["sbp"])
        if dValues["sbp"] >200 :
            print("probleme a la ligne {0} : sbp > 200".format(dValues["row.names"]))
        
        
        ### modifier toute une serie de variables d'un type texte a un type float (marche pareil pour int ... ) ; attention entre la virgule ou le point en decimal ; attention aux E-07...
        lVarFloat = ["ldl", "adiposity", "typea", "alcohol"]
        for var in lVarFloat : 
            dValues[var] = float(dValues[var])
        
        for var in self.lVariables : 
            outLine += "{0}".format(dValues[var])
            if var == self.lVariables[len(self.lVariables)-1] :
                outLine += "\n"
            else : 
                outLine += "\t"
        return outLine
        pass
    
    def createRscript(self):
        Rscript = self.generateRscript()
        Rfile = open(self._Rscript, "w")
        Rfile.write(Rscript)
        Rfile.close()
        
    def generateRscript(self):
        Rscript = ""
        Rscript += "library(shiny)\n"
        Rscript += "library(ggplot2)\n"
        Rscript += "library(scales)\n"
        
        return Rscript
        pass
        
    def run(self):
        self._checkOptions()
        self.fileParser()
        self.createRscript()
        pass



if __name__ == "__main__":
    iTemplate_Rshiny = Template_Rshiny()
    iTemplate_Rshiny.setAttributesFromCmdLine()
    iTemplate_Rshiny.run()    