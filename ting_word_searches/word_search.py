def exists_word(word, instance):
    occurrences = []
    for i in range(len(instance)):
        item = instance.search(i)
        found_occurrences = []

        for j, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                found_occurrences.append({"linha": j})

        if found_occurrences:
            occurrences.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": found_occurrences
            })

    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
