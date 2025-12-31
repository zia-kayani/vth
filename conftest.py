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
def context(browser, request):

    # Check for video recording marker
    record_video = request.node.get_closest_marker("video")
    if record_video:
        context = browser.new_context(
            record_video_dir="reports/videos/",
            record_video_size={"width": 1280, "height": 720}
        )
    else:
        context = browser.new_context()

    # Start tracing for the context
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
