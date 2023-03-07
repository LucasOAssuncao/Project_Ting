from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for file_dict in instance.queue:
        if file_dict['nome_do_arquivo'] == path_file:
            return
    
    archive_lines = txt_importer(path_file)
    num_lines = len(archive_lines)
    
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": num_lines,
        "linhas_do_arquivo": archive_lines
    }
    
    instance.enqueue(file_dict)
    print(file_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
