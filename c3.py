#!/usr/bin/python
# -*- coding: utf-8 -*-  


#Non-ASCII character problem : utf-8 -*-
#text = raw_input("prompt")  # Python 2
#text = input("prompt")  # Python 3



#f1 = open('fname1', 'r')
#f2 = open('fname2', 'r') 


#Take file names from user 
fname1 = raw_input ("Enter the first filename:" )
fname2 = raw_input ("Enter the second filename:" )

#open file for reading
f1 = open(fname1)
f2 = open(fname2)


# Print

print("Comparing files ", " > " + fname1, " < " +fname2)
print("\n")


# Read the first line from the files

f1_line = f1.readline()
f2_line = f2.readline()


# Initialize counter for line number
line_no = 1

# except KeyboardInterrupt:

# > A
# < B
# <+ B'nin farkı A'dan
# >+ A'nın farkı B'den 


# Loop for :if either file1 or file2 has not reached EOF

while f1_line != '' or f2_line != '':

    print(" ")

    # Strip the leading whitespaces
    # Önde gelen boşlukları çıkart
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    
    # Compare the lines from both file
    if f1_line != f2_line:
        
	#File2'de bir satır yoksa çıktıyı >+ işaretiyle işaretledim
        # If a line does not exist on file2 then mark the output with + sign
        if f2_line == '' and f1_line != '':
            print(">+", "Line-%d" % line_no, f1_line)

	# aksi takdirde file1'deki satırı çıkartıp > ile işaretledim 
        # otherwise output the line on file1 and mark it with > sign
        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)
            
	# File1 üzerinde bir satır yoksa çıktıyı + işaretiyle işaretledim
        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            print("<+", "Line-%d" % line_no, f2_line)

	# aksi takdirde file2 satırını çıkart ve onu < ile işaretledim
        # otherwise output the line on file2 and mark it with < sign
        elif f2_line != '':
            print("<", "Line-%d" %  line_no, f2_line)

        #print()

    #Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()


    #Increment line counter
    line_no += 1

# Close our files
f1.close()
f2.close()
