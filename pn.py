import getNgrok
def get_urls():
        urls = ""
        urls += get_href('News')
        urls += get_href('Movies')
        urls += get_href('SSH')
        urls += get_href('SCP')
        return urls

def get_url(name):
        url_dict = {'News': 'http', 'Movies': 'http', 'SSH': 'tcp', 'SCP': 'tcp'}
        getNgrok.getNgrok()
        ngrok = open('/var/lib/openshift/574de04d7628e10c4900014c/app-root/repo/ngrok.txt','r')
        for line in ngrok:
                urlToTest = line.rstrip("\n")
                if urlToTest.startswith(url_dict[name]):
                        url = generateUrl(name,urlToTest)
        ngrok.close()
        return url

def get_href(name):
        return generateHref(name,get_url(name))

def generateUrl(name,url):
        if (name == 'News'):
                return url + "/movies/news.py"
        elif (name == "Movies"):
                return url + "/movies/movies.py"
        elif (name == "SSH"):
                return url.replace('tcp://','ssh://pi@')
        elif (name == "SCP"):
                return url.replace('tcp://','scp://pi@')

def generateHref(name,url):
        if (name == 'News'):
                return "<a style=font-size:18pt href=" + url + ">News</a><br/>"
        elif (name == "Movies"):
                return "<a style=font-size:18pt href=" + url + ">Movies</a><br/>"
        elif (name == "SSH"):
                return "<a style=font-size:18pt href=" + url + ">SSH to Pi</a><br/>"
        elif (name == "SCP"):
