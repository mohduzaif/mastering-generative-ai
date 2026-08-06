from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("all_pdfs/dl-curriculum.pdf")

docs = loader.load()

# print the complete document object in the list.
# print(docs)

# print the first document object that contain in the list.
# print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata['page'])