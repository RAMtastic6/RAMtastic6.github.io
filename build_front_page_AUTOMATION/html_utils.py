def openSection(id_string: str) -> str:
    """ apre una sezione in HTML (<section>)"""
    open_section = " <section id=\"{}\">\n".format(id_string)
    return open_section

def closeSection() -> str:
    """ apre una sezione in HTML (<section>)"""
    open_section = " </section>\n"
    return open_section

def open_h2(string) -> str:
    """ apre un tag <h2> in HTML"""
    open_section = " <h2> {} </h2> \n".format(string)
    return open_section

def open_h3(string) -> str:
    """ apre un tag <h2> in HTML"""
    open_section = " <h3> {} </h3> \n".format(string)
    return open_section

def openDetails(string) -> str:
    """ apre una lista in HTML"""
    open_list = "<details> \n <summary> {} </summary>\n".format(string)
    return open_list

def closeDetails() -> str: 
    close_list = "</details>\n"
    return close_list

def openList() -> str:
    """ apre una lista in HTML"""
    open_list = "<ul>\n"
    return open_list

def closeList() -> str: 
    close_list = "</ul>\n"
    return close_list

def buildListItem(string: str) -> str:
    """ costruisce un elemento di una lista in HTML partendo da una stringa in input"""
    open_list = "<li> {} </li>".format(string)
    return open_list

def buildHtmlLink(path: str, nome_link: str) -> str:
    link = "<a href=\"" + path + "\"> " + nome_link + " </a>"
    return link