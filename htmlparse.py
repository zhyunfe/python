'''
XML 
操作xml有两种方法：DOM和SAX，DOM 会把整个XML读入内存，解析为树，因此占用内存大解析慢，优点是可以任意遍历树的节点
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件

在Python中使用SAX解析XML非常简洁，准备好start_element,end_element, char_data这三个函数就可以解析xml了
example：
<a href="/"> python </a>

会产生3个事件：
    1、 start_element事件，在读取<a href="/"> 时
    2、 char_data事件，在读取 python 时
    3、 end_element事件，在读取 </a> 时

'''
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: %s , attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax: end_element: %s' % name)
    
    def char_data(self, text):
        print('sax: char_data: %s' % text)
    
xml = r'''<?xml version="1.0"?>
  <ol>
      <li><a href="/python">Python</a></li>
      <li><a href="/ruby">Ruby</a></li>
  </ol>
'''

handler = DefaultSaxHandler()

parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)

#######################
# HTMLParser
#######################

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    
    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')
    
    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_charref(self, name):
        print('&#%s' % name)

parser = MyHTMLParser()
parser.feed('''
<html>
  <head></head>
  <body>
  <!-- test html parser -->
      <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
       廖雪峰 2018年年Python教程
 </body></html>''')