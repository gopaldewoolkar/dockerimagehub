from app import app

def test_home(): # Always start the function names with test 
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World!"