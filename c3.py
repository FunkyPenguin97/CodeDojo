#!/usr/bin/python
# -*- coding: utf-8 -*-  


#Non-ASCII character problem : utf-8 -*-
#text = raw_input("prompt")  # Python 2
#text = input("prompt")  # Python 3



#f1 = open('fname1', 'r')
#f2 = open('fname2', 'r') 


#Dosya isimlerini kullanıcıdan al
fname1 = raw_input ("Enter the first filename:" )
fname2 = raw_input ("Enter the second filename:" )

#Dosyaları oku
f1 = open(fname1)
f2 = open(fname2)


#Yazdırma kısmı

print("Comparing files ", " > " + fname1, " < " +fname2)
print("------------------------------------------------")


#Dosyaların ilk satırlarını oku

f1_line = f1.readline()
f2_line = f2.readline()


# Satır numarası için counter koy
line_no = 1

# except KeyboardInterrupt: #

# > A
# < B
# <+ B'nin farkı A'dan
# >+ A'nın farkı B'den 

#Kopya olmayanlar için sayaç
count_not_copy = 0

#Bütün satırlar için sayaç
total_line = 0

def copy_or_not():

	#print("%d" % total_line)
	#print("%d" % count_not_copy)
	k = (total_line - (count_not_copy / 2 )) 
	#print("%d" % k)
	y= ((k*100) / total_line)
	print("%d percent copy found " % y)

# EOF Control

while f1_line != '' or f2_line != '':

    #print("while'dayım******")
       
    
    # Önde gelen boşlukları çıkart
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    
    # Satırları karşılaştır
    if f1_line != f2_line:
        
	#File2'de o satır yoksa çıktıyı >+ ile işaretle
        
        if f2_line == '' and f1_line != '':
            print(">+", "Line-%d" % line_no, f1_line)
	    

	# else file1'deki satırı çıkartıp > ile işaretle
       
        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)
	    count_not_copy += 1
            
	# File1 üzerinde o satır yoksa çıktıyı <+ ile işaretle
        
        if f1_line == '' and f2_line != '':
            print("<+", "Line-%d" % line_no, f2_line)
	    

	# else file2 deki satırı çıkarttım ve onu < ile işaretle
    
        elif f2_line != '':
            print("<", "Line-%d" %  line_no, f2_line)
	    count_not_copy += 1

        #print()

    #Dosyadaki bir sonraki satırı oku
    f1_line = f1.readline()
    f2_line = f2.readline()
    total_line += 1 


    #Counter'ı arttır
    line_no += 1

# Dosyaları kapat
f1.close()
f2.close()


copy_or_not()
