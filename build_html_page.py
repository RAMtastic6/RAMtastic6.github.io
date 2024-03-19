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
    <link rel="stylesheet" href="style.css">
</head> 
<body>
    <header>
        <nav>
            <div id="logo">
                <img src="img/logo.png" alt="Logo RAMtastic6">
            </div>
            <ul>
                <li><a href="#candidatura">Candidatura</a></li>
                <li><a href="#rtb">RTB</a></li>
                <li><a href="#pb">PB</a></li>
                <li><a href="#chi-siamo">Chi siamo</a></li>
                <li><a href="#contatti">Contatti</a></li>
            </ul>
        </nav>
    </header>
    <h1>Documentazione del gruppo RAMtastic6</h1> 
"""
footer = """
<section id="chi-siamo">
        <h2>Chi siamo</h2>
        <p>Il gruppo RAMtastic6, gruppo 14 del progetto didattico di Ingegneria del Software, è composto da 6 studenti
            del corso di laurea triennale in Informatica dell'Università
            degli Studi di Padova.</p>
        <p>Il gruppo è composto da:</p>
        <ul>
            <li>Leonardo Basso</li>
            <li>Riccardo Zaupa</li>
            <li>Samuele Visentin</li>
            <li>Michele Zambon</li>
            <li>Filippo Tonietto</li>
            <li>Davide Brotto</li>
        </ul>
        <p>Riferimenti:</p>
        <ul>
            <li><a href="https://github.com/RAMtastic6/Project14">Repository GitHub del gruppo</a></li>
            <li><a href="https://www.math.unipd.it/~tullio/IS-1/2023/Dispense/PD2.pdf">Regolamento del progetto</a></li>
            <li><a href="https://www.math.unipd.it/~tullio/IS-1/2023/Progetto/C3.pdf">Capitolato Easy Meal</a>
            </li>
        </ul>
    </section>
    <section id="contatti">
        <h2>Contatti</h2>
        <p>Email: <a href="mailto:ramtastic6@gmail.com">ramtastic6@gmail.com</a></p>
    </section>
    <div id="info-finali">
        <p>Ultimo aggiornamento: 8 Marzo 2024</p>
        <p>Sito creato da Riccardo Zaupa</p>
    </div>
</body>
"""
# da questo punto, iniziano i vari periodi
 
def buildFrom(path):
    dump = ""
    dump += intestazione

    periodi = os.listdir(path) 
    periodi.sort() # riordinare i periodi

    for p in periodi:
        # prendere i dati per ogni periodo
        local_path = os.getcwd()
        documents = getFilesInDir(path + "/" + p + "/")
        verbali_interni_periodo  = getFilesInDir(os.path.join(local_path, path, p , "verbali", "verbali_interni/"))
        verbali_esterni_periodo  = getFilesInDir(os.path.join(local_path, path, p , "verbali", "verbali_esterni/")) 
        verbali_interni_periodo.sort()
        verbali_esterni_periodo.sort()

        # formattare i riferimenti
        ref_documents = formatReferencesHTML(documents, path + "/" + p + "/") # del primo non ne sono sicuro, in quanto non si apre una lista.
        ref_VIP = formatReferencesHTML(verbali_interni_periodo , path + "/" + p + "/verbali/verbali_interni/") 
        ref_VEP = formatReferencesHTML(verbali_esterni_periodo, path + "/" + p + "/verbali/verbali_esterni/") 

        # strutturare ogni periodo
        id_string = str.lower(p).replace("-", "")
        id_string = ''.join(filter(lambda x: not x.isdigit(), id_string))
        dump += openSection(id_string)
        dump += open_h2(id_string.upper() if id_string=="rtb" or id_string=="pb" else id_string.capitalize())
        dump += ref_documents
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
f = open("index.html", "w")
f.write(dump)