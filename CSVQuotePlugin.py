
class CSVQuotePlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        outfile = open(filename, 'w')

        firstline = self.infile.readline()
        contents = firstline.strip().split(',')
        outfile.write(contents[0])
        outfile.write(',')
        for i in range(1, len(contents)):
            outfile.write("\""+contents[i]+"\"")
            if (i != len(contents)-1):
                outfile.write(',')
            else:
                outfile.write('\n')
        
        for line in self.infile:
            outline = "\"" + line[:line.find(',')] + "\"" + line[line.find(','):]
            outfile.write(outline)

