from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text


class Page:


    def __init__(self, elem: Elem) -> None:
        """
        __init__() method.
        """
        if not isinstance(elem, Elem):
            raise Elem.ValidationError
        self.elem = elem


    def is_valid(self) -> bool:
        """
        This method will check if the content of the page is valid.

        Return:
            bool: True if the content is valid, False otherwise.
        """
        return self.__recursive_check(self.elem)
    

    def __str__(self) -> str:
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        """
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>\n" + str(self.elem)
        return str(self.elem)


    def write_to_file(self, filename: str) -> None:
        """
        This method will write the HTML content to a file.

        Args:
            filename (str): The name of the file.
        """
        with open(filename, 'w') as file:
            file.write(str(self))


    def __recursive_check(self, elem: Elem) -> bool:
        """
        This method will check if the content of the page is valid.

        Args:
            elem (Elem): The element to check.

        Return:
            bool: True if the content is valid, False otherwise.
        """
        if not isinstance(self.elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text)):
            return False
        
        if isinstance(elem, Html) and len(elem.content) == 2 \
            and isinstance(elem.content[0], Head) and isinstance(elem.content[1], Body):
            if all(self.__recursive_check(content) for content in elem.content):
                return True
        
        if isinstance(elem, Head) and len(elem.content) == 1 and isinstance(elem.content[0], Title):
            if self.__recursive_check(elem.content[0]):
                return True
        
        if isinstance(elem, (Body, Div)) and \
            all(isinstance(content, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for content in elem.content):
            if all(self.__recursive_check(content) for content in elem.content):
                return True
            
        if isinstance(elem, (Title, H1, H2, Li, Th, Td)) and \
            len(elem.content) == 1 and type(elem.content[0]) == Text:
            return True

        if isinstance(elem, P) and all(isinstance(content, Text) for content in elem.content):
            return True
        
        if isinstance(elem, Span) and all(isinstance(content, (Text, P)) for content in elem.content):
            return True
        
        if isinstance(elem, (Ul, Ol)) and len(elem.content) > 0 and \
            all(isinstance(content, Li) for content in elem.content):
            return True
        
        if isinstance(elem, Tr) and len(elem.content) > 0 and \
            all(isinstance(content, (Th, Td)) for content in elem.content) and \
            all(type(elem.content[0]) == type(content) for content in elem.content):
            return True
        
        if isinstance(elem, Table) and all(isinstance(content, Tr) for content in elem.content):
            return True
        
        return False
    


def __test_node() -> None:

    # Test 1

    html = Html([
            Head([
                Title(content=Text('"Hello ground!"'))
            ]),
            Body([
                H1(content=Text('"Oh no, not again!"')), 
            ])
        ])
    page = Page(html)
    if page.is_valid():
        print("__test_node() 1 success")
    else:
        print("__test_node() 1 failure")
    
    # Test 2

    html = Html([
            Head([
                Title(content=Text('"Hello ground!"'))
            ]),
            Body([
                H1(content=Text('"Oh no, not again!"')),
                Img(attr={'src':'http://i.imgur.com/pfp3T.jpg'})
            ])
        ])
    page = Page(html)
    if not page.is_valid():
        print("__test_node() 2 success")
    else:
        print("__test_node() 2 failure")


def __test_html_head() -> None:

    # Test 1

    html = Html([
            Head([
                Title(content=Text('"Hello ground!"'))
            ]),
            Body([])
        ])
    page = Page(html)
    if page.is_valid():
        print("__test_html_head() 1 success")
    else:
        print("__test_html_head() 1 failure")

    # Test 2

    html = Html([
            Body([]),
            Head([]),
        ])
    page = Page(html)
    if not page.is_valid():
        print("__test_html_head() 2 success")
    else:
        print("__test_html_head() 2 failure")

    # Test 3

    html = Html([])
    page = Page(html)
    if not page.is_valid():
        print("__test_html_head() 3 success")
    else:
        print("__test_html_head() 3 failure")


def tester() -> None:
    __test_node()
    __test_html_head()
    __test_title_h1_h2_li_th_td_p_span()
    __test_ul_ol()
    __test_tr()
    __test_table()


if __name__ == "__main__":
    tester()