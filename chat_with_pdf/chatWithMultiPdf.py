import streamlit as st
import utils as ut
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.embeddings import HuggingFaceEmbeddings

class ChatPdf:

    def get_pdf_text(self,pdf_docs):
        text=""
        for pdf in pdf_docs:
            pdf_reader=PdfReader(pdf)
            print(pdf_reader)
            for page in pdf_reader.pages:
                text+=page.extract_text()
        return text
    
    def get_chunks(self,pdf_text):
        text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
        chunks = text_splitter.split_text(pdf_text)
        return chunks
    
    def get_vectorstore(self,text_chunks):
        embeddings = HuggingFaceEmbeddings()
        # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        return vectorstore

    def get_conversation_chain(self,vectorstore):
        

        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=ut.llm_azure,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain


    def handle_userinput(self,user_question):
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
        
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)



if __name__ =='__main__':
    chat_with_multi_pdf=ChatPdf()
    st.set_page_config(page_title="Chat with multiple pdf",page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    st.header("Chat with multiple PDF's :books:")
    user_question= st.text_input("Ask a question about your documents:")
    if user_question:
        chat_with_multi_pdf.handle_userinput(user_question)
    
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs=st.file_uploader("upload your PDFs here and click on 'Process",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
               # get pdf text
                pdf_text=chat_with_multi_pdf.get_pdf_text(pdf_docs)

                #get pdf text into chunks
                chunks=chat_with_multi_pdf.get_chunks(pdf_text)

                #create vector store database
                
                vectorstore = chat_with_multi_pdf.get_vectorstore(chunks)

                # create conversation chain
                st.session_state.conversation = chat_with_multi_pdf.get_conversation_chain(
                    vectorstore)


