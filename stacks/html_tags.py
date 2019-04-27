from stack_linked_list import LinkedListStack


def match_html_tags(html_data):
    """
    Returns true if all opening HTML tags have corresponding closing tags
    >>> match_html_tags("<h1>Hello</h1>")
    True
    >>> match_html_tags("<h1>Hello</h2>")
    False
    >>> match_html_tags("<head><title>Hello</title><head>")
    False
    >>> match_html_tags("<head><title>Hello</title></head>")
    True
    >>> match_html_tags("<head><title>Hello<title>")
    False
    """
    S = LinkedListStack()

    # find the position of the first left angle bracket
    left_bracket = html_data.find("<")
    while left_bracket != -1:
        # find the position of the corresponding right angle bracket
        right_bracket = html_data.find(">", left_bracket + 1)
        if right_bracket == -1:
            return False

        # get the tag
        tag = html_data[left_bracket + 1:right_bracket]

        # determine if it is a closing or opening tag. If it is an opening tag, add it to the stack else check for its corresponding opening tag on the stack
        if tag.startswith("/"):
            if S._is_empty():
                return False
            opening_tag = S.pop().value
            if opening_tag != tag[1:]:
                return False
        else:
            S.push(tag)
        # find the next left bracket
        left_bracket = html_data.find("<", right_bracket + 1)
    # checks if all opening tags have been matched at the end of the script
    return S._is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
