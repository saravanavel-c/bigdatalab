def test_application():
    message = "CI/CD Pipeline is working successfully!"
    assert "CI/CD" in message

test_application()
print("Test passed!")