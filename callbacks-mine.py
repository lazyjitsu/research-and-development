from langchain.callbacks.base import BaseCallbackHandler


class AgentCallbackHandler(BaseCallbackHandler):
    def __init__(self, agent):
        super().__init__(agent)
        self.agent = agent

    def on_agent_action(self, action):
        print(f"on_agent_action {action=}")
        if action.name == "get_text_length":
            print(f"get_text_length invoked with {action.input=}")
            action.output = len(action.input["text"])
            self.agent.send_action(action)
        else:
            raise ValueError(f"Unknown action {action.name}")

    def on_agent_finish(self, finish):
        print(f"on_agent_finish {finish=}")
        self.agent.send_finish(finish)
