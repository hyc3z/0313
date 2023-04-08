# Information to connect to your ACS instance.
location = "westus2"
subscription_id = "46d053ee-9156-4361-a443-28c40516fc67"
resource_group = "test-search"
search_service_name = "search-test-tprompt"
index_name = "test-tprompt-index"
semantic_config_name = "default" # name of the config. can leave it as deafult

# Setup connection, create ACS instance and an index
from azure.identity import AzureCliCredential
from tpromptlib.indexes import AzureSearchIndex
AzureSearchIndex.create_acs_instance(
    search_service_name=search_service_name,
    subscription_id=subscription_id,
    resource_group=resource_group,
    location=location,
    credential=AzureCliCredential()
)

AzureSearchIndex.create_search_index(
    search_service_name=search_service_name,
    index_name=index_name,
    subscription_id=subscription_id,
    resource_group=resource_group,
    semantic_config_name=semantic_config_name,
    credential=AzureCliCredential()
)
# Parse and Chunk your data
from tpromptlib.chunking import TextChunker

document_path = 'sample_documentation'

result = TextChunker(version="v2", extensions_to_process=["md", "py", "html"]).chunk_directory(document_path,
                                                                                       num_tokens=1024,
                                                                                       url_prefix=None,
                                                                                       token_overlap=0)

print(f"Processed {result.total_files}")
print(f"Unsupported formats: {result.num_unsupported_format_files}")
print(f"Files with errors: {result.num_files_with_errors}")
print(f"Found {len(result.chunks)} chunks")

# Upload data to ACS
AzureSearchIndex.upload_documents(
    docs=result.chunks,
    search_service_name=search_service_name,
    index_name=index_name,
    subscription_id=subscription_id,
    resource_group=resource_group
)