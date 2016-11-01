wget  -r  -np -k -p http://www.fda.gov/Drugs/InformationOnDrugs/ApprovedDrugs/ucm279174.htm
python script/shortlink.py
wget -i download.list -P www.fda.gov/Drugs/InformationOnDrugs/ApprovedDrugs/