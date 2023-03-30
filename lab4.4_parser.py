import pandas as pd
import dicttocsv
str_csv = """{id,name 
1,"Johnson, Smith, and Jones Co." 
2,"Sam ""Mad Dog"" Smith" 
3,Barney & Company 
4,Johnson's Automotive
           }"""

def jsoncsvparser(json_file):
    json_file = pd.read_csv('str_csv', orient='index')
    json_file = str_csv.to_json(index=False)
    print(str_csv)


jsoncsvparser(str_csv)