from pydantic import BaseModel

class ServerRequest(BaseModel):
    command: str
    metadata: float
    