from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# create the object of loaders.
loader = PyPDFLoader('../Langchain_Loaders/all_pdfs/dl-curriculum.pdf')

# load the documnet from the pdf.
docs = loader.load()
# print(docs)

# create the object of text-splitter.
splitter = CharacterTextSplitter(
    chunk_size = 100, 
    chunk_overlap = 10, 
    separator = ''
)

# create the chunks.
chunks = splitter.split_documents(docs)

# print the chunnks
print(chunks[0])
print(chunks[1])
