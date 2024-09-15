import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "credentials"

# Initialize the chat model
llm = ChatOpenAI(model="gpt-4", temperature=0)

def parse_with_openai(dom_chunks, parse_description):
    parsed_results = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        # Create the system and human messages
        messages = [
            SystemMessage(
                content="""
                youll read scraped data and answer to users query like basic questions, summary, comparison etc. 
                """
            ),
            HumanMessage(
                content=f"Here is the DOM content: {chunk}. The description is: {parse_description}"
            )
        ]

        # Call the LLM and get the result
        response = llm(messages)
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        
        # Append the result
        parsed_results.append(response.content)

    return "\n".join(parsed_results)