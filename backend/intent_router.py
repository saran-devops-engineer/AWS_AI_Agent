from llm_client import query_llama
from aws_tasks import list_unused_eips, list_running_instances, describe_all

def extract_intent_from_message(message):
    prompt = f"""
You are an AWS assistant. Based on the user's message, classify the intent into one of the following categories:

- list_unused_eips: When the user asks for unused elastic IPs or unattached EIPs.
- list_running_instances: When the user wants to know what EC2 instances are currently running.
- describe_all: When the user wants to list all EIPs regardless of usage.
- general: Anything else that doesn't match the above.

Only return the intent. Do NOT explain anything. Just output one of these: list_unused_eips, list_running_instances, describe_all, general.

User message: \"{message}\"
"""
    intent = query_llama(prompt).strip().lower()
    if intent in ["list_unused_eips", "list_running_instances", "describe_all"]:
        return intent
    return "general"

def handle_intent(intent, message):
    if intent == "list_unused_eips":
        return list_unused_eips()
    elif intent == "list_running_instances":
        return list_running_instances()
    elif intent == "describe_all":
        return describe_all()
    else:
        return query_llama(message)
