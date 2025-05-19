from typing import List, Callable
from dotenv import load_dotenv
load_dotenv()

def function_tool(func):
    """Decorador dummy, para que compile el código. Puedes expandirlo luego."""
    return func

class Agent:
    def __init__(self, name: str, instructions: str, tools: List[Callable]):
        self.name = name
        self.instructions = instructions
        self.tools = tools or []

    def run(self, pregunta):
        # Comportamiento por defecto, redirige pregunta al primer tool disponible
        if self.tools:
            tool = self.tools[0]
            return tool(pregunta)
        return f"[{self.name}] No hay herramientas definidas para responder: {pregunta}"
