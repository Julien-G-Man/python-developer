"""Simple trial I'm using :) """

import logging

logger = logging.getLogger(__name__)

class BaseTool:
    def execute(self, **kwargs):
        raise NotImplementedError

class SearchTool(BaseTool):
    def execute(self, query, **kwargs):
        return f"Searching for {query}"

class CalculatorTool(BaseTool):
    def execute(self, expression, **kwargs):
        return eval(expression)  # careful in real systems

class DBQueryTool(BaseTool):
    def execute(self, query, **kwargs):
        return f"DB result for {query}"


TOOLS = {
    "search": SearchTool,
    "calculator": CalculatorTool,
    "db_query": DBQueryTool
}

class ToolFactory:
    @staticmethod
    def create(tool_name):
        try:
            if tool_name not in TOOLS:
                raise ValueError(f"Tool '{tool_name}' not found")
            return TOOLS.get(tool_name)()   
        except Exception as e:
            logger.error("Error: ", e)
            
class ToolExecutor:
    def __init__(self, tool_name):
        self.tool = ToolFactory.create(tool_name)
        
    def run(self, **kwargs):
        return self.tool.execute(**kwargs)    