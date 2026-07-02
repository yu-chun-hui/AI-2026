from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import ModelClientStreamingChunkEvent
import llms

agent = AssistantAgent(
    name="poet_agent",
    model_client=llms.deepseek_model_client,
    system_message="""你是一位古代诗人，擅于编写文言文古诗。""",
    model_client_stream=True,
)

async def main():
    task_message = "编写一首关于'冬天'的文言文古诗。内容不少于100字"
    async for event in agent.run_stream(task=task_message):
        if isinstance(event, ModelClientStreamingChunkEvent):
            print(event.content, end="")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())