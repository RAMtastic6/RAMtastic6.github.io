import os

path = "DOCUMENTI"


# ritorna una lista di stringhe
# ogni stringa rappresenta il nome di un file
# presente all'interno della cartella file_path
def getFilesInDir(dir_path: str) -> list[str]:
    """ 
    Funzione che ritorna i nomi di tutti i file all'interno di una cartella

    dir_path := path della cartella nella quale cercare i file; 
    il path deve essere formattato in modo da contenere uno slash alla fine di esso
    """
    files = [f for f in os.listdir(dir_path) if os.path.isfile(dir_path + f)]
    return files 

# aggiunge una stringa al file senza sovrascriverlo
# file_path: string
# content: string
def append(file_path, content):
    f = open(file_path, "a")
    f.write(content)
    f.close()

# aggiunge lista di elementi al file senza sovrascriverlo
# file_path: string
# items: string array
def appendItems(file_path, items = []):
    f = open(file_path, "a")
    f.write(items)
    f.close()

print(os.path.join(os.getcwd(), path,  "verbali/"))