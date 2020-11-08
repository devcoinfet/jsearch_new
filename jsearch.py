import sys
import argparse
import os
from requests_module import requests_module
from file_module import file_handler
import json

try:
    from bs4 import BeautifulSoup
    import requests
    
except ImportError as e:
    print("[+] install requirements. pip3 install -r requirements.txt")
    print(f"{e}")
    sys.exit(1)


def main():

    filename = sys.argv[0]
    parse = argparse.ArgumentParser(description="Usage: {} -u <URL> -o output".format(filename))
    parse.add_argument('-u', "--url", type=str, required=False, help="[+] URL to craw")
    parse.add_argument('-n', "--name", type=str, required=True, help="[+] Name of company ex: \n python3 jsearch.py -u https://google.com -n google")
    parse.add_argument('-d', "--directory", type=str, required=True, help="[+] Name of directory containing javascript files ex: \n python3 jsearch.py -d /tmp/javascripts")

    menu = parse.parse_args()

    if len(sys.argv[1:]) == 0:
        print(parse.print_help())
    
    if menu.url and menu.name:
       jsearch = requests_module.CoreRequests(menu.url, menu.name)
       jsearch.get_content_html()
       #code has been moded to act this way only if fed these params
    

   
    if menu.directory and menu.name:
       
       file_module_info  = file_handler.FileTracker(menu.directory,menu.name)
       
       print(menu.directory)
       print(file_module_info)
       #here take in directory and grab content from it
       directory_search = file_module_info.file_searcher()
       if file_module_info.found_hits:
          total_finds = len(file_module_info.found_hits)
          print(str(total_finds)+'\n')
          for finds in file_module_info.found_hits:
              print(json.loads(finds))
               
      
       
if __name__ == "__main__":
    main()
