# learnings
```
r=requests.get('https://finance.yahoo.com/quote/FB/')
soup=bs4.BeautifulSoup(r.content,"lxml")
price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text#,{'class':"",'data-reactid':"13"})
if price is not None and len(price) > 0:
 print(price)
 ```
