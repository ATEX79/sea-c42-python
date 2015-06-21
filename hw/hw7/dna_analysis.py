# Name: Matt Biggers
# Homework 7: DNA

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0
# Number of A seen so far.
a_count = 0
# Number of T seen so far.
t_count = 0
# Number of G seen so far.
g_count = 0
# Number of C seen so far.
c_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

    # as with C or G, this does the same for A and T.
    if bp == 'A' or bp == 'T':
        at_count = at_count + 1

    # the follow 4 if statements count A, C, G, T individually.
    if bp == 'A':
        a_count = a_count + 1
    if bp == 'C':
        c_count = c_count + 1
    if bp == 'G':
        g_count = g_count + 1
    if bp == 'T':
        t_count = t_count + 1


# divide the gc_count and the at_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count
# gc_final variable was created for Problem 6.
gc_final = (g_count + c_count) / (a_count + c_count + g_count + t_count)

# GC and AT content outputs.
print ("GC-content (float):", gc_content)
print ("AT-content:", at_content)
# Individual counts and Sum_Count is for Problem 5.
print ("A-count:", a_count, "T-count:", t_count)
print ("G-count:", g_count, "C-count:", c_count)
print ("Sum Count:", (a_count + t_count + g_count + c_count))
# Various printed outputs for Problem 6.
print ("Total Count:", total_count)
print ("Sequence Length:", len(seq))
print ("GC-Content Final:", gc_final)
print ("GC Difference:", gc_final - gc_content)
# Ouput for Problem 7 --> AT/GC ratio.
print ("AT/GC Ratio:", ((a_count + t_count) / (g_count + c_count)))

# Problem 8 - this part of the program will calculate GC content in organisms
# using a function containing if/else statements.


def gc_class():
    if gc_final >= 0.6:
        print ("This organism has a HIGH GC-Content of", gc_final, ".")
    if gc_final < 0.4:
        print ("This organism has a LOW GC-Content of", gc_final, ".")
    if gc_final >= 0.4 and gc_final < 0.6:
        print ("This organism has a MODERATE GC-Content of", gc_final, ".")


gc_class()
