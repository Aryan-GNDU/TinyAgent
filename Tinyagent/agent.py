from Tinyagent.llm import Trajectory, LLM
from Tinyagent.memory import Memory
class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(
            self,
            llm:LLM,
            memory:Memory,
                 ):
        self.llm = llm
        self.memory = memory 
        self.tools = None
        self.planner = None

        self.trajectory = Trajectory()


    def run(self, task: str):
        """Run agent on task"""
        self.memory.add("user", task)
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self) -> str:
        """Perform a single step."""
        # Generate response and add to memory
        response = self.llm.generate(self.memory.get_messages())
        self.memory.add("assistant", response.content)
        self.trajectory.add(response)
        return response.content
    
    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""
        return f"Executed action: {action}" 

