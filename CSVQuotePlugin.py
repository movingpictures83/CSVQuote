def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_quoted(s):
    return (len(s) != 0 and s[0] == '\"' and s[len(s)-1] == '\"')

class CSVQuotePlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        outfile = open(filename, 'w')

        for line in self.infile:
            contents = line.strip().split(',')
            for i in range(len(contents)):
                if (not is_number(contents[i]) and not is_quoted(contents[i])):
                    contents[i] = '\"' + contents[i] + '\"'
                outfile.write(contents[i])
                if (i != len(contents)-1):
                    outfile.write(',')
                else:
                    outfile.write('\n')
        # Old version, just quoted header and first column
        # New version above more flexible, checks if quoted already and if number
        #firstline = self.infile.readline()
        #contents = firstline.strip().split(',')
        #outfile.write(contents[0])
        #outfile.write(',')
        #for i in range(1, len(contents)):
        #    outfile.write("\""+contents[i]+"\"")
        #    if (i != len(contents)-1):
        #        outfile.write(',')
        #    else:
        #        outfile.write('\n')
        #
        #for line in self.infile:
        #    outline = "\"" + line[:line.find(',')] + "\"" + line[line.find(','):]
        #    outfile.write(outline)

