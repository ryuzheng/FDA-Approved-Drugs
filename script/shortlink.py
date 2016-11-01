folder="/home/ubuntu/workspace/www.fda.gov/Drugs/InformationOnDrugs/ApprovedDrugs/"

import os,re,sys,fileinput

for parent,dirnames,filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith("htm"):
            # print(filename)
            for x in fileinput.input(os.path.join(parent,filename),inplace=1):
                # print(x)
                if re.search(r"<a href=\"http://www.accessdata.fda.gov/drugsatfda_docs\S+.pdf\">",x):
                    # print(re.search(r"<a href=\"http://www.accessdata.fda.gov/drugsatfda_docs\S+.pdf\">",x).group(0))
                    with open("download.list",'a')as f2:
                        f2.write(re.search(r"<a href=\"http://www.accessdata.fda.gov/drugsatfda_docs\S+.pdf\">",x).group(0).replace("<a href=\"","").replace("\">","")+"\n")
                        print(re.sub(r"http://www.accessdata.fda.gov/drugsatfda_docs/label/\d+/","",x))
                else:
                    print(x)