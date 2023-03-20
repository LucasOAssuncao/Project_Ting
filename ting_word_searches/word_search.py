def exists_word(word, instance):
    occurrences = []
    for i in range(len(instance)):
        item = instance.search(i)
        found_occurrences = []

        for j, line in enumerate(item["linhas_do_arquivo"]):
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
    files_info = exists_word(word, instance, show_content=True)

    for file_info in files_info:
        for occurrence in file_info["ocorrencias"]:
            line_number = occurrence["linha"]
            line_content = occurrence["conteudo"]

            print(f'"{word}" found in file "{file_info["arquivo"]}", line {line_number}: {line_content}')
