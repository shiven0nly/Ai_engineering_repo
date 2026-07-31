# Functions:
# -> ChatRequest
# -> ChatResponse
# (Using Pydantic Models)

# Now, frontend sends this:
# {
#     "message":"Tell me about yourself"
# }

# we have to implement pydantic for this

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message:str
    
class ChatResponse(BaseModel):
    response:str