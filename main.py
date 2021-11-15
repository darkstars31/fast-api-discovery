from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from dao import get_firestore_context

app = FastAPI()
db = get_firestore_context()

keypadRuleCollection = "keypadCodeRule"

class KeycodeRule(BaseModel):
	id: Optional[str]
	companyId: Optional[int]
	name: str
	companyKeypadCodeIds: List[int]
	typeId: int
	targetId: int

class Asset(BaseModel):
	id: int
	description: str
	color: str = Field( None, title="Physical Color of the Asset", max_length=100)
	tags: List[str] = []

@app.get("/health")
async def root():
	return { "msg": "Healthy, maybe"}

@app.get("/db/assets")
async def get_all_assets():
	return {"a": "asset"}

@app.get("/db/assets/{id}")
async def get_asset( id: int, q: Optional[str] = None):
	return q

@app.get("/companies/{companyId}/keycode/rule/{id}")
async def get_keypad_rule( companyId: int, id: str ):
	keypadRule = db.collection(keypadRuleCollection).document(id).get().to_dict()
	if keypadRule["companyId"] != companyId:
		raise HTTPException(status_code=404, detail="Item not found")
	return keypadRule

@app.get("/companies/{companyId}/keycode/rules")
async def get_keypad_rules( companyId: int):
	docRefList = db.collection(keypadRuleCollection).get()
	keypadRulesList = [docRef.to_dict() for docRef in docRefList if docRef.to_dict()["companyId"] == companyId];
	return keypadRulesList

@app.post("/companies/{companyId}/keycode/rule", response_model=KeycodeRule)
async def create_keypad_rule( companyId: int, keycodeRule: KeycodeRule):
	keycodeRule.companyId = companyId
	docRef = db.collection(keypadRuleCollection).document()
	keycodeRule.id = docRef.id
	docRef.set(jsonable_encoder(keycodeRule))
	return docRef.get().to_dict()

@app.patch("/companies/{companyId}/keycode/rule/{id}", response_model=KeycodeRule)
async def update_keypad_rule( companyId: int, id: str, keycodeRule: KeycodeRule):
	docRef = db.collection(keypadRuleCollection).document(id)
	if docRef.get().exists and docRef.get().to_dict()["companyId"] == companyId:
		keycodeRule.id = docRef.id
		docRef.update(jsonable_encoder(keycodeRule))
	else: raise HTTPException(status_code=404, detail="Keypad Code Rule doesn't exist or you do not have permission to modify.")
	return docRef.get().to_dict()

@app.delete("/companies/{companyId}/keycode/rule/{id}", status_code=201)
async def delete_keypad_rule( companyId: int, id: str):
	docRef = db.collection(keypadRuleCollection).document(id)
	if docRef.get().exists and docRef.get().to_dict()["companyId"] == companyId:
		docRef.delete()
	else:
		raise HTTPException(status_code=404, detail="Keypad Code Rule doesn't exist or you do not have permission to modify.")