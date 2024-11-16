from functools import reduce
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
             )


    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        
        if not self.props:
                return ''
                
        def func(acc, tuple_pair):
            key, value = tuple_pair
            acc += f' {key}="{value}"'
            return acc
        return reduce(func, self.props.items(), "")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children, None)

    def to_html(self):
        if self.tag is None: 
            raise ValueError("Invalid HTML: no tag")
        elif not self.children:
            raise ValueError("Invalid HTML: no children")
        else:
            result = ""
            for item in self.children:
                result += item.to_html()
            return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"