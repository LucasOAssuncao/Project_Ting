from ting_file_management.file_management import txt_importer
import sys
import os

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
    num_instances = len(instance.queue)
    if num_instances == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        file_path = instance.dequeue()["nome_do_arquivo"]
        try:
            os.remove(file_path)
            print(f"Arquivo {file_path} removido com sucesso", file=sys.stdout)
        except OSError as error:
            print(f"Ocorreu um erro ao remover o arquivo {file_path}: {error}", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
