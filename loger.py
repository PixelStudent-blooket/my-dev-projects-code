import logging

def setup_logging():
    """Configures system-wide logging format."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(module)s: %(message)s",
        filename="company_audit.log"
    )
    return logging.getLogger("CompanyApp")


