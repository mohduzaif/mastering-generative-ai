from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader(
    path = 'all_pdfs', 
    glob = '*.pdf', 
    loader_cls = PyPDFLoader, 
    recursive = True
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)