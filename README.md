# learnings
### 1) web scraping yahoo FB shares
BeautifulSoup(r.content,"lxml") - "lxml " was main thing
```
r=requests.get('https://finance.yahoo.com/quote/FB/')
soup=bs4.BeautifulSoup(r.content,"lxml")
price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text#,{'class':"",'data-reactid':"13"})
if price is not None and len(price) > 0:
 print(price)
 ```
### 2) email extract re and url

    fhand = urllib.request.urlopen('https://cit.ac.in/departments/cse/academic') 
     
    for line in fhand: 
    # Getting the text file 
    # content line by line. 
    s = line.decode().strip()
    reg = re.findall(r"[A-Za-z0-9._%+-]+"
                     r"@[A-Za-z0-9.-]+"
                     r"\.[A-Za-z]{2,4}", s) 
