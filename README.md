# python_markdown_nofollow

example

```python
import markdown
from python_markdown_nofollow import LinkChangeExtension

text = '[example]() \n[example](http://example.com/) \n[example](javascript:) \n[example](#) \n[example](mailto:example@example.com) \n[example](https://example.com/)'

print(markdown.markdown(text, extensions=[LinkChangeExtension()]))
```