from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader(
    path = 'all_pdfs', 
    glob = '*.pdf', 
    loader_cls = PyPDFLoader, 
    recursive = True
)

docs = loader.load()


print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)