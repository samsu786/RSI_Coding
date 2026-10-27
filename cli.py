from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


llm = ChatGroq(
    model_name="openai/gpt-oss-120b",
    temperature=0.7
)

category_mapping = ["technical_support"]
result = input("Query:")
print(result)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", """Classify the User query using below given categorie list and 
#             proivde the confidence score as well.
#         Category_List :  technical_support, billing, general_inquiry, other
#         Output Format JSON: {
#         category: it should be one of the category from above list
#         confidence : Low | Med | High
#         }
#         """),
#     ("user", "{input}")
# ])

# chain = prompt | llm


# result = chain.invoke({"input":str(result)})
# print(json.dumps(result, indent=2))

sys_inst = """
Classify the User query using below given categorie list and 
            proivde the confidence score as well.
        Category_List :  technical_support, billing, general_inquiry, other
        Output Format JSON: {
        category: it should be one of the category from above list
        confidence : Low | Med | High}
"""


result = llm.invoke(sys_inst + "query: result")
print(result)