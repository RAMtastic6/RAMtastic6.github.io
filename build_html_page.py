from build_front_page_AUTOMATION.reference_utils import * 
from build_front_page_AUTOMATION.html_utils import *

# stringa di intestazione da scrivere
# all'inizio del file
intestazione = """<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAMtastic6</title>
    <meta name="keywords" content="RAMtastic6, Ingegneria del Software, Università degli Studi di Padova, swe, unipd">
    <meta name="description" content="Pagina di presentazione del gruppo RAMtastic6 per il progetto di Ingegneria del Software A.A. 2023/24">
    <meta name="author" content="RAMtastic6">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="img/logo.png">
</head> 
<body>
    <header>
        <nav>
            <div id="logo">
                <img src="img/logo.png" alt="Logo RAMtastic6">
                <p>RAMtastic6</p>
            </div>
            <ul>
                <li><a href="#pb">PB</a></li>
                <li><a href="#rtb">RTB</a></li>
                <li><a href="#candidatura">Candidatura</a></li>             
                <li><a href="https://github.com/orgs/RAMtastic6/repositories" target="_blank">GitHub</a></li>
                <li><a href="#chi-siamo">Chi siamo</a></li>
                <li><a href="#contatti">Contatti</a></li>
            </ul>
        </nav>
    </header>
    <main>
    <h1>Documentazione del gruppo</h1> 
"""
footer = """
<section id="chi-siamo">
        <h2>Chi siamo</h2>
        <hr>
        <p>Il gruppo RAMtastic6, il numero 14 del progetto didattico di Ingegneria del Software, è composto da 6 studenti
            del corso di laurea triennale in Informatica dell'Università
            degli Studi di Padova.</p>
        <h3>I componenti</h3>
        <ul id="membri">
            <li>Leonardo Basso</li>
            <li>Riccardo Zaupa</li>
            <li>Samuele Visentin</li>
            <li>Michele Zambon</li>
            <li>Filippo Tonietto</li>
            <li>Davide Brotto</li>
        </ul>
    </section>
    <section id="contatti">
        <h2>Contatti</h2>
        <hr>
        <p>Email: <a href="mailto:ramtastic6@gmail.com">ramtastic6@gmail.com</a></p>
        <p>Riferimenti:</p>
        <ul>
            <li><a href="https://github.com/RAMtastic6/Project14" target=\"_blank\">Repository GitHub del gruppo riservato alla documentazione</a></li>
            <li><a href="https://github.com/RAMtastic6/Proof-of-Concept" target=\"_blank\">Repository GitHub del gruppo riservato al Proof of Concept</a></li>
            <li><a href="https://github.com/RAMtastic6/EasyMeal" target=\"_blank\">Repository GitHub del gruppo riservato al MVP</a></li>
            <li><a href="https://www.math.unipd.it/~tullio/IS-1/2023/Dispense/PD2.pdf" target=\"_blank\">Regolamento del progetto</a></li>
            <li><a href="https://www.math.unipd.it/~tullio/IS-1/2023/Progetto/C3.pdf" target=\"_blank\">Capitolato Easy Meal</a>
            </li>
        </ul>
    </section>
    
    </main>
    <footer>
    
    <p>© <span lang="en">Copyright</span> 2024 RAMtastic6 - Tutti i diritti riservati</p>    
    </footer>
</body>
</html>
"""
# da questo punto, iniziano i vari periodi

## lista di documenti esterni per le sezioni RTB e PB
nomi_docs_esterni = ["Analisi_dei_Requisiti", "Piano_di_Qualifica", "Piano_di_Progetto", "Glossario", "Manuale_Utente", "Specifica_Tecnica"]

## lista di documenti interni per le sezioni RTB e PB
nomi_docs_interni = ["Norme_di_Progetto"]
 
def buildFrom(path):
    dump = ""
    dump += intestazione

    periodi = os.listdir(path) 
    periodi.sort(reverse=True) # invertire la lista dei periodi

    for p in periodi:
        # prendere i dati per ogni periodo
        local_path = os.getcwd()
        documents = getFilesInDir(os.path.join(path, p ))
        verbali_interni_periodo  = getFilesInDir(os.path.join(local_path, path, p , "verbali", "verbali_interni"))
        verbali_esterni_periodo  = getFilesInDir(os.path.join(local_path, path, p , "verbali", "verbali_esterni")) 
        verbali_interni_periodo.sort(reverse=True)
        verbali_esterni_periodo.sort(reverse=True)

        # separare i documenti esterni e interni
        documents_esterni = []
        documents_interni = []
        for d in documents:
            if any(doc in d for doc in nomi_docs_esterni):
                documents_esterni.append(d)
            if any(doc in d for doc in nomi_docs_interni):
                documents_interni.append(d)
        # rimuovere i documenti esterni e interni dalla lista dei documenti
        documents = [d for d in documents if d not in documents_esterni]
        documents = [d for d in documents if d not in documents_interni]
        
        # formattare i riferimenti
        ref_documents_esterni = formatReferencesHTML(documents_esterni, path + "/" + p + "/")
        ref_documents_interni = formatReferencesHTML(documents_interni, path + "/" + p + "/")
        ref_documents = formatReferencesHTML(documents, path + "/" + p + "/") # del primo non ne sono sicuro, in quanto non si apre una lista.
        ref_VIP = formatReferencesHTML(verbali_interni_periodo , path + "/" + p + "/verbali/verbali_interni/") 
        ref_VEP = formatReferencesHTML(verbali_esterni_periodo, path + "/" + p + "/verbali/verbali_esterni/") 

        # strutturare ogni periodo
        id_string = str.lower(p).replace("-", "")
        id_string = ''.join(filter(lambda x: not x.isdigit(), id_string))
        dump += openSection(id_string)
        is_rtb_or_pb = id_string=="rtb" or id_string=="pb"
        dump += open_h2(id_string.capitalize() if not is_rtb_or_pb else id_string.upper())
        dump += "<hr>"
        dump += ref_documents
        if is_rtb_or_pb:
            dump += open_h3("Documenti Esterni")
            dump += ref_documents_esterni
            dump += open_h3("Documenti Interni")
            dump += ref_documents_interni
        
        dump += open_h3("Verbali")

        # prendere lista verbali interni e formattare link
        dump += openDetails("Interni")
        dump += openList()
        dump += ref_VIP 
        dump += closeList()
        dump += closeDetails()

        # prendere lista verbali esterni e formattare link
        dump += openDetails("Esterni")
        dump += openList()
        dump += ref_VEP 
        dump += closeList()
        dump += closeDetails()

        dump += closeSection()

    dump += footer 
    return dump

dump = buildFrom("documenti")
f = open("index.html", "w", encoding="utf-8")
f.write(dump)