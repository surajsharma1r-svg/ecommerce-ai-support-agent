from app.tool_registry import TOOLS


def execute_tool(tool_name, arguments):

    if tool_name not in TOOLS:
        return {
            "error": f"Unknown tool: {tool_name}"
        }

    tool_function = TOOLS[tool_name]

    result = tool_function(**arguments)

    return result