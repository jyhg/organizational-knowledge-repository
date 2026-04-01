"""Performance testing with Locust.

Run: locust -f locustfile.py --host=http://localhost:8000
"""

from locust import HttpUser, task, between


class KnowledgeBaseUser(HttpUser):
    """Simulates a user querying the knowledge base."""

    wait_time = between(1, 5)

    @task(3)
    def chat_query(self):
        """Send a chat query to the knowledge base."""
        self.client.post(
            "/api/chat",
            json={"message": "供应商准入的注册资本要求是多少？"},
        )

    @task(1)
    def list_documents(self):
        """List documents in the knowledge base."""
        self.client.get("/api/docs")

    @task(1)
    def health_check(self):
        """Check system health."""
        self.client.get("/health")
