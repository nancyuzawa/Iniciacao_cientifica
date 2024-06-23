f_urls = open('campinas-sp-gov-br-urls.txt', 'a')
arquivopdf = open('urls_pdf.txt', 'a')
arquivocsv = open('urls_csv.txt', 'a')
arquivodoc = open('urls_doc.txt', 'a')
arquivortf = open('urls_rtf.txt', 'a')
arquivoxls = open('urls_xls.txt', 'a')
arquivodocx = open('urls_docx.txt', 'a')
arquivoxlsx = open('urls_xlsx.txt', 'a')
arquivoother = open('urls_other.txt', 'a')
#print(f_urls.read())
filepath = 'campinas-sp-gov-br-urls.txt'
#contadorpdf=0
#contadorcsv=0
#contadordoc=0
#contadorrtf=0
#contadorxls=0
#contadordocx=0
#contadorxlsx=0
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
       a=len(line)
       if(a!=0):
           e=line[a-5]
           b=line[a-4]
           c=line[a-3]
           d=line[a-2]
           if(b=="p" and c=="d" and d=="f"):
               print("Line {}: {}".format(cnt, line.strip()))
               #contadordpf+=1
               #print(contador)
               arquivopdf.writelines(line) 
           elif(b=="c" and c=="s" and d=="v"):
               #contadorcsv+=1
               arquivocsv.writelines(line) 
           elif(b=="d" and c=="o" and d=="c"):
               #contadordoc+=1
               arquivodoc.writelines(line) 
           elif(b=="r" and c=="t" and d=="f"):
               #contadorrtf+=1
               arquivortf.writelines(line) 
           elif(b=="x" and c=="l" and d=="s"):
               #contadorxls+=1
               arquivoxls.writelines(line) 
           elif(e=="d" and b=="o" and c=="c" and d=="x"):
               #contadordocx+=1
               arquivodocx.writelines(line) 
           elif(e=="x" and b=="l" and c=="s" and d=="x"):
               #contadorxlsx+=1
               arquivoxlsx.writelines(line) 
           else:
               arquivoother.writelines(line) 
