#! env python
# -*- coding: utf-8 -*-

import os
import sys

def makeMapFile(arg_number_of_row, arg_number_of_col):
    print("makeMapFile")
    numberOfRow = int(arg_number_of_row)
    numberOfCol = int(arg_number_of_col)

    if((numberOfRow <= 0) or (numberOfCol <= 0)):
        print("Invalid Value of Argument. Expected Vaule is morae than 0")
        return
    indexFilePath = './index.html'
    indexFile = open(indexFilePath, 'w')
    textForIndexFile = [
        "<!DOCTYPE html>\n",
        "<html lang=\"ja\">\n",
        "<head>\n",
        "\t<meta charset=\"UTF-8\">\n",
        "\t<title>水中MAP⭐️</title>\n",
        "\t<link rel=\"stylesheet\" href=\"style.css\">\n",
        "</head>\n",
        "<body>\n",
        "<h1>水中MAP⭐️</h1>\n",
        "<table border=\"1\">\n",
    #   table elements will be inserted at later step. tableElementIndex:10 is reserved  
        "</table>\n",
        "</body>",
        "</html>"
    ]
    indexFile.writelines(textForIndexFile)
    indexFile.close()
    indexFile = open(indexFilePath,'r')
    indexFileLines = indexFile.readlines() 
    indexFile.close()
    tableElementIndex = 10
    for j in range(numberOfCol):
        indexFileLines.insert(tableElementIndex, '\t<tr>\n')
        tableElementIndex = tableElementIndex+1
        for i in range(numberOfRow):
            print('%d\t%d' % (j,i))
            mapFilePath = './' + str(j) + str(i)+ '.html'
            mapFile = open(mapFilePath, 'w')
            textForMap = [
                "<!DOCTYPE html>\n",
                "<html lang=\"ja\">\n",
                "<head>\n",
                "\t<meta charset=\"UTF-8\">\n",
#               title will be inserted at later step. titleIndex:5 is reserved  
                "\t<link rel=\"stylesheet\" href=\"area.css\">\n",
                "</head>\n",
                "<body>\n",
                "<h1>XXX -yym</h1>\n",
                "\n",
                "<!-- begin wwww.htmlcommentbox.com -->\n"
                "<div id=\"HCB_comment_box\"><a href=\"http://www.htmlcommentbox.com\">HTML Comment Box</a> is loading comments...</div>\n",
                "<link rel=\"stylesheet\" type=\"text/css\" href=\"https://www.htmlcommentbox.com/static/skins/bootstrap/twitter-bootstrap.css?v=0\" />\n",
                "<script type=\"text/javascript\" id=\"hcb\"> /*<!--*/ if(!window.hcb_user){hcb_user={};} (function(){var s=document.createElement(\"script\"), l=hcb_user.PAGE || (\"\"+window.location).replace(/'/g,\"%27\"), h=\"https://www.htmlcommentbox.com\";s.setAttribute(\"type\",\"text/javascript\");s.setAttribute(\"src\", h+\"/jread?page=\"+encodeURIComponent(l).replace(\"+\",\"%2B\")+\"&mod=%241%24wq1rdBcg%2450Bq0kJISS4Kc93tBhUgS%2F\"+\"&opts=16862&num=10&ts=1614058531818\");if (typeof s!=\"undefined\") document.getElementsByTagName(\"head\")[0].appendChild(s);})(); /*-->*/ </script>\n",
                "<!-- end www.htmlcommentbox.com -->\n",
                "\n",
                "<a href=\"index.html\">Back to Top</a>\n",
                "</body>"
            ]
            titleIndex = 5
            textForMap.insert(titleIndex, '\t<title>mapNo:%d-%d</title>\n' %(j,i))
            mapFile.writelines(textForMap)
            mapFile.close()
            indexFileLines.insert(tableElementIndex, '\t\t<td><a href=\"%d%d.html\"></a></td>\n' % (j,i))
            tableElementIndex = tableElementIndex + 1
        indexFileLines.insert(tableElementIndex, '\t</tr>\n')
        tableElementIndex = tableElementIndex + 1
    indexFileLines.insert(tableElementIndex, '</table>\n')

    indexFile = open(indexFilePath, 'w')
    indexFile.writelines(indexFileLines)
    indexFile.close()
    return

def main():
    if len(sys.argv) == 3:
        print('row:%s\tcol:%s' % (sys.argv[1], sys.argv[2]))
        makeMapFile(sys.argv[1], sys.argv[2])
    else:
        print("Invalid Number Of Argument. Expected command format is 'python genMapHtml.py number_of_row number_of_col'")
    return

if __name__ == '__main__':
    main()
