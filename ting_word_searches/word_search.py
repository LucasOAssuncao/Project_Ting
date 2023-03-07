import os
import io


def exists_word(word, instance):
    occurrences = []
    for i in range(len(instance)):
        item = instance.search(i)
        lines_found = []

        for j, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                lines_found.append({"linha": j})

        if lines_found:
            occurrences.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": lines_found
            })

    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
