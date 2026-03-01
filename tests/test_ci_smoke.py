import os


def test_import_dependencies():
    """
    Smoke test to ensure all critical dependencies install correctly.
    """
    import langchain
    import langgraph
    import langchain_community
    import langchain_core
    import langchain_groq
    import langchain_openai
    import faiss
    import streamlit
    import tavily


def test_required_env_vars_exist():
    """
    Ensures required GitHub Secrets are available during CI.
    """
    required_vars = [
        "DOCKER_PASSWORD",
        "DOCKER_USERNAME",
        "HF_TOKEN"
    ]

    for var in required_vars:
        assert os.getenv(var) is not None, f"{var} is missing"