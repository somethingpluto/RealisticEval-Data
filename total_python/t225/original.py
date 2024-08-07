def load_and_chunk_texts(pdf_directory, documents, embedder_id):
    texts = []
    for doc in documents:
        filename = doc["filename"]
        if embedder_id not in doc["embedders"]:
            print(f"Embedder {embedder_id} configuration not found for {filename}. Skipping.")
            continue
        chunk_size = doc["embedders"][embedder_id]["chunk_size"]
        overlap = doc["embedders"][embedder_id]["overlap"]
        pdf_path = os.path.join(pdf_directory, filename)

        # Text Splitting, including overlap created using ChatGPT
        try:
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text = page.get_text()
                    words = text.split()
                    for i in range(0, len(words), chunk_size - overlap):
                        chunk = ' '.join(words[i:i + chunk_size])
                        texts.append(chunk)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    return texts