def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if target_document_id == document_id:
            return level
        # Recursively search deeper
        if nested_documents[document_id]:
            result = count_nested_levels(nested_documents[document_id], target_document_id, level + 1)
            if result != -1:  # Found the document in a nested level
                return result
    return -1  # Return -1 if the document was not found

