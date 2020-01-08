class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self._head_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._head_contents:
            self.contents+=str(tag)
        
        super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up seperatly
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        
        super().display(file=file)

class HTMLDoc(object):

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file )

if __name__ == '__main__':
    my_page = HTMLDoc()
    my_page._head.add_tag("title","Page Title")
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page.')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)

    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, agrregation uses existing instances"
        " of ojbect to build up another object.")
    new_body.add_tag('p', "The composed ojbect doesn't actually own the objects that it's composed of"
        " - if it's destroyed, those objects continue to exist. ")

    # give our document new content by swtiching it's body
    my_page._body = new_body
    with open('test2.html', "w") as test_doc:
        my_page.display(file=test_doc)