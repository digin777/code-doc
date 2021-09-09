from typing import Match
import re

tokens=[
    "@h1",
"@h2",
"@h3",
"@h4",
"@h5",
"@h6",
"@s"
]
tockdic={
 "@h1":{"open":"<h1>","close":"</h1>"},
"@h2":{"open":"<h2>","close":"</h2>"},
"@h3":{"open":"<h3>","close":"</h3>"},
"@h4":{"open":"<h4>","close":"</h4>"},
"@h5":{"open":"<h5>","close":"</h5>"},
"@h6":{"open":"<h6>","close":"</h6>"},
"@s":{"open":"<strong>","close":"</strong>"}
}
def main(doc):

    lines = doc.split("\n")
    out=""
    for line in lines:
        for token in tokens:
            match=re.search(token,line)
            if match:
                out+=line[:match.start()]+tockdic[token]["open"]+line[match.end():]+tockdic[token]["close"]
                break
        else:
            out+="<p>"+line+"</br>"

    
    print(out)
    with open("out.html","w") as f:
        f.write("<body>"+out+"</body>")
if __name__=="__main__":
    text='''@h1 hai iam sona 
    @h3 faster @faster 
    @h3 sorry
    @h2 somtimes i have dreams
    @h3 nothing
    @h6 samsung 
    @s solid selection
    ✨Magic ✨
    fdfsd
    @h3 dfd
'''
    main(text)