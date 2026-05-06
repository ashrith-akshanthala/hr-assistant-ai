from langchain.agents import create_agent
from langchain.messages import HumanMessage

from app.llm.v1.context.request import RequestContext
from app.llm.v1.core.model import model_llama3_2_3b
from app.llm.v1.core.registry import get_tools
from app.llm.v1.prompts.system import get_system_prompt

model = model_llama3_2_3b
tools = get_tools()


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=get_system_prompt(),
    context_schema=RequestContext,
)


def invoke_agent(message: str, context: RequestContext):
    messages = {"messages": [HumanMessage(message)]}

    result = agent.invoke(
        messages,
        context=context,
    )
    for chat_message in result["messages"]:
        chat_message.pretty_print()

    return result["messages"][-1].content
