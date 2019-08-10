import requests

def sendAPIcheckRequest():
    url='https://blockchain.info/q/addressbalance/1KnBUi7JmK1EFTbYdxUMdGaXQdwK455zKT'
    answer=requests.get(url)
    return answer.content

CompFile=open("Comp.html",'w')
amount=sendAPIcheckRequest()
CompFile.truncate()
CompFile.write(str(amount))
