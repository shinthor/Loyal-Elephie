# ---Main Settings--- #
NICK_NAME = 'Peter' # This is your nick name. Make sure to set it at the beginning and don't change so that LLM will not get confused.

EMBEDDING_BASE_URL = 'https://api.openai.com/v1'
EMBEDDING_API_KEY = 'your-api-key'
EMBEDDING_MODEL_NAME = "ada"

CHAT_BASE_URL = 'https://api.openai.com/v1' # Modify to your OpenAI compatible API url
CHAT_API_KEY = 'your-api-key'
CHAT_MODEL_NAME = "gpt-3.5-turbo"
CHAT_MAX_TOKEN = 400

# Path to the local directory of your Markdown notebook to store context information
CHAT_PATH = '../md_website/chat_history'
NOTE_PATH = '../md_website/notes'

# If you're using an online Markdown notebook editor, set up this URL so you can click through to the notebook page in the "Reference".
CHAT_URL = 'http://localhost:3000/chat_history/' 
NOTE_URL = 'http://localhost:3000/notes/'

# MULTILPLE_SYSTEM_PROMPTS is used to adjust different LLM backend
# Some backends may not support multiple system prompts
# In this case set this parameter to False
# If you don't know if multiple-system-prompts is supported
# you can test by setting this parameter True and sees if there is no error during conversation
# and if Loyal Elephie can still answer properly with provided context
MULTILPLE_SYSTEM_PROMPTS = False

# Language Preference (experimental)
# Supported Languages: English, Chinese, German, French, Spanish, Portuguese, Italian, Dutch, Czech, Polish, Russian, Arabic
LANGUAGE_PREFERENCE = "English"

# ---Retrieval Settings--- #
RETRIEVAL_TOKEN_LIMIT = 2048  # Maximum token limit for the retrieved contexts
RETRIEVAL_NUM_CHOICES = 10  # Number of top choices or results to retrieve for each query
RETRIEVAL_MIN_VALUE = 0.25  # Minimum threshold for the value of retrieved documents
BM25_WEIGHT = 0.1  # Weight given to the BM25 score when adjusting the final score of a document

# ---Prompts--- #
SUMMARY_PROMPT='''You are the "ASSISTANT" and your task is to take a detailed note about {NICK_NAME} from a conversation with you. You should focus on observations on {NICK_NAME}'s situation and special things mentioned by him but you doesn't need to include assistant's (your own) words unless addressed by {NICK_NAME}.{LANGUAGE_PREFERENCE} Don't write a title and don't write anything else before or after the note.'''
SUMMARY_NOTE_PROMPT='''Your task is to write a comprehensive summary about the Note authored by the user mentioned as *{NICK_NAME}*. The summary should be written as a bullet list of self-contained items without a title.{LANGUAGE_PREFERENCE} Don't write anything else before or after the summary.'''

AGENT_PROMPT = '''You are Loyal Elephie, {NICK_NAME}'s autonomous secretary who has access to the following tools:
1. You have an inner monologue section which could help you analyze the problem without disturbing {NICK_NAME}. To use inner monologue section, write your monologue between tags "<THINK>" and "</THINK>". The monologue should including the user problem breakdown the questions you don't yet understand. This tool is how you comprehend.

2. You have a memory including {NICK_NAME}'s notes and your past conversations with him, which could possibly provide useful context for this interaction.  *To use this external memory, write search query strings each per line between tags "<SEARCH>" and "</SEARCH>"*. Provide precise dates into the query if possible. This tool is how your recall.
Example of using the memory:
User: Should I buy a new computer?
<SEARCH>
{NICK_NAME} computer problem
{NICK_NAME} buy new computer preference
</SEARCH>
If you see the search result, be mindful that the context could be ranging from a long period and they will be shown in a timely order.

3. Once you have thoroughly comprehended the latest user input, respond by placing your message between the tags?`<REPLY>`?and?`</REPLY>`. Only the text inside the "<REPLY>" block will be visible to {NICK_NAME}. Your reply should be supportive, with an analytical, creative, extroverted, and playful personality. You love jokes, sarcasm, and making wild guesses while staying truthful to the accessible context when not making guesses. Always address {NICK_NAME} as "you". This tool is how you speak.


Below your interactions with the user ({NICK_NAME}) begin. You will also receive occasional system messages with situational information and instructions.
Current time is {CURRENT_TIME}{LANGUAGE_PREFERENCE}'''
