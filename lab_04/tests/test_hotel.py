from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)



def test_get_hotels():

    response = client.get("/hotels/")

    assert response.status_code == 200