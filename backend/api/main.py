from fastapi import FastAPI
from api import role


app = FastAPI(
    title="HyeTheater API",
    description="Hye Theater is an open-source community website that shares Armenian culture with the new generation.",  # noqa: E501
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    # Hide Schema
)


app.include_router(role.router)


@app.get("/api/v1/test", tags=["test"])
def get_test():
    return {"test": "test_return"}
