import urllib.request, re, sys

def saveRawPage(url):
    page = urllib.request.urlopen(url)
    mybytes = page.read()
    savedPage = mybytes.decode("utf8")
    print(savedPage)
    return savedPage

def saveAllLinks(page):
    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', savedPage)
    print(urls)
    return urls

# Saves unique host to hostList and number of occurances in hostCnt dictionary
def saveHosts(urls):
    hostList=[]
    for url in urls:
        p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
        m = re.search(p,url)
        hostList.append(m.group('host'))
    hostCnt = {i:hostList.count(i) for i in hostList}
    hostList = list(dict.fromkeys(hostList))
    return hostList, hostCnt

def saveEmailAddresses(page):
    matchList = re.findall(r'[\w\.-]+@[\w\.-]+', page)
    return matchList
    
def countImgLinks(page):
    imgNum = len(re.findall(r'img.*src\s*=\s*"(.+?)"', page))
    return imgNum

if(len(sys.argv) != 2):
    print("Invalid nuber of arguments provided")
    sys.exit(1)

savedPage=saveRawPage(sys.argv[1])
urls=saveAllLinks(savedPage)
hostList, hostCnt=saveHosts(urls)
emailAddressList=saveEmailAddresses(savedPage)
imgNum=countImgLinks(savedPage)