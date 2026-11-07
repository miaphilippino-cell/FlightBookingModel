from security.validators import Validators # type: ignore
from security.rate_limiter import RateLimiter # pyright: ignore[reportMissingImports]


def test_email_validation():
    assert Validators.validate_email("mia@email.com")


def test_rate_limiter():
    limiter = RateLimiter(max_requests=2, time_window=60)

    assert limiter.allow_request("mia")
    assert limiter.allow_request("mia")
    assert not limiter.allow_request("mia")