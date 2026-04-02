"""API tests for /api/chat endpoint (in-process via TestClient)."""


def test_chat_returns_200(client):
    """Chat endpoint should return 200 with valid input."""
    response = client.post("/api/chat", json={"message": "什么是安全库存预警？"})
    assert response.status_code == 200


def test_chat_response_structure(client):
    """Response should contain answer, sources, and conversation_id."""
    response = client.post("/api/chat", json={"message": "供应商准入标准"})
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert "conversation_id" in data
    assert isinstance(data["sources"], list)


def test_chat_empty_message(client):
    """Empty message should be handled gracefully."""
    response = client.post("/api/chat", json={"message": ""})
    assert response.status_code in (200, 422)
