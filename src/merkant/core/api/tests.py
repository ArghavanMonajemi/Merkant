def test_unknown_url_returns_json_404(api_client):
    response = api_client.get("/api/does-not-exist/")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "not_found"