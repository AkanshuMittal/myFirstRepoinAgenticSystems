# policy_retrieval.py

chunks = [
    {
        "text": "Mobiles can be returned within 7 days if damaged.",
        "metadata": {
            "doc_type": "policy",
            "product": "mobile",
            "status": "active",
            "source_file": "mobile_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops can be returned within 10 days for manufacturing defects.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops were earlier returnable within 30 days.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "archived",
            "source_file": "old_laptop_policy.md",
            "section_title": "Old Return Rules",
        },
    },
    {
        "text": "For laptop battery drain, run diagnostics mode before replacing parts.",
        "metadata": {
            "doc_type": "manual",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_service_manual.pdf",
            "section_title": "Battery Diagnostics",
        },
    },
    {
        "text": "Premium users get billing support within 24 hours.",
        "metadata": {
            "doc_type": "policy",
            "product": "billing",
            "status": "active",
            "source_file": "billing_policy.md",
            "section_title": "Premium Support",
        },
    },
]


def matches_filters(metadata: dict, filters: dict) -> bool:
    """
    Return True only if every key-value pair in filters
    matches the metadata.
    """
    for key, value in filters.items():
        if metadata.get(key) != value:
            return False
    return True


def retrieve(filters: dict) -> list:
    """
    Return all chunks whose metadata satisfies the filters.
    """
    results = []

    for chunk in chunks:
        if matches_filters(chunk["metadata"], filters):
            results.append(chunk)

    return results


def format_citation(chunk: dict) -> str:
    """
    Return citation in the required format.
    """
    metadata = chunk["metadata"]
    return f"Source: {metadata['source_file']} - {metadata['section_title']}"


def print_retrieval_results(filters: dict) -> None:
    """
    Print retrieved chunks with citations.
    """
    results = retrieve(filters)

    if not results:
        print("No matching chunks found.")
        return

    for chunk in results:
        print(chunk["text"])
        print(format_citation(chunk))
        print()


if __name__ == "__main__":

    # Test 1
    print_retrieval_results(
        {
            "doc_type": "policy",
            "product": "laptop",
            "status": "active",
        }
    )

    # Test 2
    print_retrieval_results(
        {
            "doc_type": "policy",
            "product": "mobile",
            "status": "active",
        }
    )

    # Test 3
    print_retrieval_results(
        {
            "doc_type": "manual",
            "product": "laptop",
            "status": "active",
        }
    )