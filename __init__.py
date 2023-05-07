# import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
 
class LinkChangeTreeprocessor(Treeprocessor):  
    def run(self, root):
        start_url = (('http://', 'https://'),
                    ('#', 'javascript:', 'mailto:', '\x02amp\x03#109;\x02amp\x03#97;\x02amp\x03#105;\x02amp\x03#108;\x02amp\x03#116;\x02amp\x03#111;\x02amp\x03#58;'))
        
        for elem in root.iter('a'):
            link_url = elem.get('href').lower() or ''
            if link_url.startswith(start_url[0]) and not link_url.startswith(start_url[1]):
                elem.set('rel', 'nofollow')
 
class LinkChangeExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(LinkChangeTreeprocessor(md), 'link_nofollow', -999)