import tempfile
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

def process_uploaded_files(uploaded_files):
    """
    Process multiple uploaded files.
    Supports PDF and TXT.
    """

    all_documents = []

    for uploaded_file in uploaded_files:

        # detect extension
        suffix = "." + uploaded_file.name.split(".")[-1]

        # create temporary file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as tmp:

            tmp.write(uploaded_file.getvalue())
            temp_path = tmp.name

        # choose loader
        if uploaded_file.name.endswith(".pdf"):

            loader = PyPDFLoader(temp_path)

        elif uploaded_file.name.endswith(".txt"):

            loader = TextLoader(temp_path)

        else:

            raise ValueError(
                "Unsupported file type"
            )

        docs = loader.load()

        all_documents.extend(docs)

    return all_documents