import pytest
from dotenv import load_dotenv
from config.env_config import ENV_CONFIG

# Load environment variables once
load_dotenv(override=True)

# ---------- pytest hooks ----------
def pytest_addoption(parser):
    parser.addoption("--env", default="qa")

# ---------- session fixtures ----------
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(env):
    return ENV_CONFIG[env]["base_url"]

# ---------- browser fixtures ----------
@pytest.fixture
def context(browser):
    context = browser.new_context()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    context.tracing.stop(path="reports/tracing/tracing.zip")
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()
