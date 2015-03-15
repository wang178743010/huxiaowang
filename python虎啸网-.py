#coding:utf-8
import requests,re
url = 'http://www.huxiu.com/tagslist/all.html'
r = requests.get(url).content
def a():
    s = re.findall(r'<li class="js-tag-w(.*?)</li>',r,re.S)
    return s
def b(lj):
    dict = {}
    for x in s:
        try:
            z = x.find('href="')
            link = lj+x[z+6:].split('"')[0]
            z = x[2:].find('>')
            name = x[z+3:].split('<')[0]
            dict.setdefault(name,link)
        except:
            pass
    return dict
#----------------------------------------------------------------------
def c():
    for x,y in dict.items():
        print x.decode("utf-8").encode("gbk")
        d(y)
        print '-------------------------------------------------------------------'
#----------------------------------------------------------------------
def d(url):
    r = requests.get(url).content
    s = re.search('<ul class="pagination">(.*?)</ul>',r,re.S)
    if s:
        z = s.group()  
        p = re.findall('href="(.*?)"',z,re.S)
        max = f(p)
        e(url,max)
    else:
        pass
#----------------------------------------------------------------------
def e(url,max):
    old_url = url[:-5]+'/'
    max_url=g(old_url+str(max))
    j = 1   #序号
    i = 1
    while i<=int(max):
        s = requests.get(old_url+str(i)).content
        for x in re.findall('<h3>(.*?)target="_blank">(.*?)</a>(.*?)<div class="mob-sub">',s,re.S):
            try:
                y = x[1].decode("utf-8").encode("gbk")
                print '     ',j,'.',y
                j+=1
            except:
                pass
        i=i+1

#--------------------下面是两个过滤方法--------------------------------------------------
def f(s):               
    zx = ''
    if s:
        zy = s[len(s)-1]+'/'
        for x in zy:
            if x in '0123456789/':
               zx = zx + x
        zx = zx.split('/')[3]
        return zx
    else:
        return 1
def g(s):
    zp = ''
    for x in s:
        if x not in ' ':
            zp = zp + x
    return zp
print '=======================等您来检阅======================='

#_________________________________这里才是程序的开始__________________________________________
s = a()
dict = b('http://www.huxiu.com/')
c()
url,max = d(url)

















