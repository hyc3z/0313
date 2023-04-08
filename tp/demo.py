"""
End to end script to demo how we can use stateless documentation chatbot for enterprise chat gpt usecase
Provide the following env vars: CHATGPT_URI, CHATGPT_KEY, AZURE_URL, AZURE_KEY and run the main function to test
Command line based chatbot.
"""
import os

from tpromptlib.datamodels.prompt_models import TPromptInput, OAIGenerationConfig
from tpromptlib.document_searchers import AzureDocumentSearcher
from tpromptlib.prompts.bots import DocumentationChatbot
from tpromptlib.prompts.models.llm import GPTEndpoint
from tpromptlib.state import TPromptState

if __name__ == "__main__":
    chatgpt_url = os.environ.get("CHATGPT_URI")
    chatgpt_key = os.environ.get("CHATGPT_KEY")
    azure_document_search_api_key = os.environ.get("AZURE_KEY")
    # print("Get env:\n gpt_url:{} \ngpt_key:{} \n search_key:{}".format(chatgpt_url, chatgpt_key, azure_document_search_api_key))
    azure_document_search_index = "test-tprompt-index"
    azure_document_search_configuration = "default"
    query_type = "semantic"
    azure_document_search_servicename = "search-test-tprompt"

    azure_doc_searcher = AzureDocumentSearcher(
        api_key=azure_document_search_api_key,
        index_name=azure_document_search_index,
        service_name=azure_document_search_servicename,
        query_type=query_type,
        semantic_configuration_name=azure_document_search_configuration,
    )

    oai_config = OAIGenerationConfig(temperature=0.0, top_p=1.0, max_tokens=1000, stop=["<|im_end|>"])
    llm = GPTEndpoint(api_key=chatgpt_key, api_url=chatgpt_url, auth_manager=None, oai_config=oai_config)
    
    chatbot = DocumentationChatbot(
        doc_searcher=azure_doc_searcher, llm=llm,
        enable_intent=True, enable_citation=True, top_k=5 
    )
    
    tprompt_state = TPromptState()
    while True:
        user_query = input("Please ask your question:\n")
        tprompt_state.add_user_message(user_query)
        tprompt_input = TPromptInput(
            doc_search_top_k=5,
            user_query=user_query,
        )
        tprompt_reply = chatbot.reply(tprompt_input, tprompt_state)
        print(tprompt_reply.reply)
        tprompt_state.update_state(tprompt_reply.reply, tprompt_reply.intent)
