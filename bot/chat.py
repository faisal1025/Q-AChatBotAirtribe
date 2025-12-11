import os
from chroma.storage import semantic_search
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def user_query(prompt):
    print(f"User Query: {prompt}")
    # retrival
    relevent_context = semantic_search(prompt)
    # augment
#     prompt = f"""
#     provide a professional response of the following query

#     #context:
#     {relevent_context}

#     #question:
#     {prompt}

# """
    # generate
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": f"You are a helpful client support assistant. Having this context:\n {relevent_context}"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content