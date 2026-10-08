def fetch_status():
    return {"status": "healthy", "service": "git-lab-api", "version": "1.0"}

def get_endpoints():
    return ["/api/v1/health", "/api/v1/user", "/api/v1/metrics"]
