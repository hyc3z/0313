a = "ie2ivru3gsawsii7w4qycc7bhy2kogrzdr3h5jp3hf6e63sifxya"
from azureml.core import Workspace
subscription_id = 'your_subscription_id'
resource_group = 'your_resource_group_name'
workspace_name = 'your_workspace_name'
workspace = Workspace(subscription_id, resource_group, workspace_name)
pat_token = "your_pat_token"
target = "https://pkgs.dev.azure.com/TScience"
workspace.set_connection(name="TPrompt", 
  category = "PythonFeed",
  target = target, 
  authType = "PAT", 
  value = pat_token) 