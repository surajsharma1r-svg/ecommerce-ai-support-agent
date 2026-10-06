def build_context(results):
    context_parts = []

    for result in results:
        context_parts.append(
            f"Source:{result['file_name']}\n"
            f"content:{result['content']}"
        )

        context ="\n\n".join(context_parts)
    return context  