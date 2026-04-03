#!/usr/bin/env python3
"""Test script for MiniMax API integration."""
import asyncio
import httpx
from anthropic import AsyncAnthropic


async def test_minimax_direct():
    """Test MiniMax API via Anthropic-compatible endpoint."""
    api_key = "sk-cp-dYLtCg3ZEYhCiegEZ1UCEHelOfa6akinI_NNrohm-zJCYMFL-EfNtcFCFdO7W-Rk0pySyMJQGAFwFJNhT8qqssOc0ytkJjcOIdTgxob4WHxcNHqOdLZqXyw"
    base_url = "https://api.minimaxi.com/anthropic"
    model = "MiniMax-M2.7"

    print(f"Testing MiniMax API...")
    print(f"Base URL: {base_url}")
    print(f"Model: {model}")
    print("-" * 50)

    http_client = None
    try:
        # Create client with proxy bypass (httpx 0.27+ uses proxy=None, not proxies)
        http_client = httpx.AsyncClient(proxy=None, timeout=60.0)
        client = AsyncAnthropic(
            api_key=api_key,
            base_url=base_url,
            http_client=http_client
        )

        # Test simple message
        print("Sending test message...")
        message = await client.messages.create(
            model=model,
            max_tokens=200,
            messages=[{"role": "user", "content": "你好，请用一句话介绍你自己。"}]
        )

        print(f"✓ Success!")
        print(f"Total content blocks: {len(message.content)}")

        # Print all content blocks
        for i, block in enumerate(message.content):
            print(f"\nBlock {i+1} type: {type(block).__name__}")
            if hasattr(block, 'text'):
                print(f"  Text: {block.text}")
            elif hasattr(block, 'thinking'):
                print(f"  Thinking: {block.thinking}")

        print(f"\nModel: {message.model}")
        print(f"Usage: {message.usage}")

    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if http_client:
            await http_client.aclose()


if __name__ == "__main__":
    asyncio.run(test_minimax_direct())
