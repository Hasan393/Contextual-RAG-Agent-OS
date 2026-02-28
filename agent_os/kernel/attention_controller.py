def compress_memory(model, memory_hierarchy):
    if len(memory_hierarchy.short_term) > 4:
        text_to_compress = "\n".join(memory_hierarchy.short_term)
        prompt = f"Summarize the following conversation into a dense core memory for long-term storage:\n{text_to_compress}"
        
        response = model.generate_content(prompt)
        compressed_memory = response.text.strip()
        
        memory_hierarchy.add_long_term(compressed_memory)
        memory_hierarchy.short_term = memory_hierarchy.short_term[-2:]
        
        return compressed_memory
    return None