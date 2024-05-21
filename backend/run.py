if __name__ == "__main__":
    import uvicorn
    # Use an import string here to facilitate reloading
    uvicorn.run("api.main:app", reload=True, host="0.0.0.0", port=8000)
else:
    # Add app to local scope for application runtime to discover app
    from api.main import app  # noqa: F401 pylint: disable=unused-import
