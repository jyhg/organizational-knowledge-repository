from app.rag.pipeline import RetrievedContext

SYSTEM_PROMPT = """你是一个企业供应链知识库助手。根据提供的上下文信息回答用户问题。
规则：
1. 只根据提供的上下文回答，不要编造信息
2. 如果上下文中没有相关信息，明确告知用户
3. 回答要准确、专业、简洁
4. 如有需要，引用来源文档"""


class AnswerGenerator:
    """Generate answers from retrieved contexts using LLM."""

    async def generate(self, question: str, contexts: list[RetrievedContext]) -> str:
        """Generate an answer based on question and retrieved contexts."""
        _context_text = "\n\n".join(f"[来源: {ctx.source}]\n{ctx.content}" for ctx in contexts)
        # TODO: call LLM via llm_gateway
        return f"[待集成LLM] 问题: {question}, 上下文数量: {len(contexts)}"
