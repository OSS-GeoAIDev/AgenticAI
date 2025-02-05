from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain import PromptTemplate

# Define the prompt template
template = "Translate the following English text to French: {text}"
prompt = PromptTemplate(template=template, input_variables=["text"])

# Initialize the OpenAI model
llm = OpenAI(api_key="your_openai_api_key")

# Create the LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Define the input text
input_text = "Hello, how are you?"

# Run the chain
output = chain.run({"text": input_text})

print(output)