from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
import backend.app.models as models
from backend.dependencies import get_current_user

router = APIRouter(prefix="/seller", tags=["seller"])

@router.post("/upload_proof")
def upload_proof(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    if current_user.role != "seller":
        raise HTTPException(status_code=403, detail="Only sellers can upload proof")

    fake_url = f"/static/{file.filename}"
    current_user.proof_url = fake_url
    current_user.verification_status = "pending"

    db.commit()
    db.refresh(current_user)

    return {"message": "Proof uploaded, awaiting verification", "proof_url": fake_url}
