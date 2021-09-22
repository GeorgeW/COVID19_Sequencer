from Bio import SeqIO
from Bio.Data import CodonTable

class Genetic_Code_Runner:
    info = "Sequencing COVID-19"

    def function(self):
        #print("Doing something with the genetic code")
        input_file = open("sequences.fasta", "r")
        output_file = open("nucleotides_covid19.tsv", "w")
        output_file.write("Gene\tA\tC\tG\tT\tLength\tCG%\n")

        for seq_record in SeqIO.parse(input_file, "fasta"):
            #define variables for each letter of nucleotide
            gene_name = seq_record.name
            a = seq_record.seq.count("A")
            c = seq_record.seq.count("C")
            g = seq_record.seq.count("G")
            t = seq_record.seq.count("T")
            #define cg percentage
            length = len(seq_record.seq)
            cg_percent = float(c + g ) / length
            output_line = '%s\t%i\t%i\t%i\t%i\t%i\t%f\n' % \
(gene_name, a, c, g, t, length, cg_percent)

            #write to file
            output_file.write(output_line)

        output_file.close()
        input_file.close()
        return "Finished processing.."
# set class to sequence variable
sequence = Genetic_Code_Runner()
sequence.function()

