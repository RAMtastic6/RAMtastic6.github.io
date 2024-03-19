import re
from build_front_page_AUTOMATION.file_utils import *
from build_front_page_AUTOMATION.html_utils import *


path = "DOCUMENTI/2-RTB/verbali/interni/"

# ritorna una stringa s
# s è la formattazione di un link ad un file  
# in linguaggio markdown

# funzione che prende in input una stringa 
# (nel caso di interesse, il nome di un file quale verbale o altro documento)
# e ne ritorna il nome nel formato da utilizzare per il link all'interno
# della pagina github.io
# per buildare il link anche i nomi dei file dobrebbero essere formattati in un certo modo:
# in particolare il carattere speciale .
# dovrebbe essere solamente riservato all'estensione del file e non al numero di versione
# per quello si potrebbe usare il carattere -
def build_link_name(path: str = "") -> str:

    # estensioni da rimuovere
    ext = [".pdf", ".txt"]
    link_name = path

    # rimuovere estensione file
    for e in ext:
        if e in link_name:
            link_name = link_name.replace(e, "")

    # separare gli elementi 
    link_items = link_name.split("_")
    link_name = ""
    for i in link_items:
        link_name += i 
        link_name += " "
    link_name = link_name.rstrip()
    return link_name
    
def formatReferences(items: list[str] = [], path: str = "") -> str:
    s = ""
    for i in items:
        nome_link = build_link_name(i)
        s += " - [" + nome_link + "](" + path + "/" + i + ")"
        c = checkForVersioning(i)
        if c:
            version_number = c.group()          
            s += " (" + version_number + ")<br> \n"
        else:
            s += "<br> \n"
    return s

def formatReferencesHTML(items: list[str] = [], path: str = "") -> str:
    s = ""
    for i in items:
        # TODO: formattare la stringa in modo che rispetti
        # lo standard html
        nome_link = build_link_name(i)
        path_to_link = path + i
        item = buildHtmlLink(path_to_link, nome_link) 
        item = buildListItem(item)
        s += item + "\n"
    return s

def checkForVersioning(string: str):
    """ Ritorna un Match object se una stringa contiene informazioni di versionamento """
    version_regex = "v[0-9].[0-9].[0-9]"
    match = re.search(version_regex, string)
    if match:
        return match 
    return None 

# def addVersioningInfo(string, version):
#     string += " (" + version + ")"
#     return string

# DEBUG
# path_to_verbale = "verbale_10_maggio_2024"
# path_to_AR = "analisi_dei_requisiti_v_10-4-2.txt"
# print(build_link_name(path_to_AR))

# d = getFilesInDir(path)
# s = formatReferencesHTML(d, path)
# print(s)