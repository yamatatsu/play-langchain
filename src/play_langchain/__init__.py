from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage


def main() -> int:
    print("Hello from play-langchain!")
    return 0


def chat() -> None:
    model = ChatBedrock(
        model="anthropic.claude-3-5-sonnet-20240620-v1:0", beta_use_converse_api=True
    )

    messages = [
        SystemMessage(content="Translate the following from English into Japanese"),
        HumanMessage(content="hi!"),
    ]
    model.invoke(messages)
