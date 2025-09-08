# backend/routes/ar_routes.py

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
from backend.dependencies import get_current_user
from PIL import Image
import uuid
import os

router = APIRouter(prefix="/ar", tags=["ar"])

UPLOAD_DIR = "static/ar_previews"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/preview")
async def ar_preview(
    wall: UploadFile = File(...),
    artwork: UploadFile = File(...),
    current_user=Depends(get_current_user),
):
    try:
        wall_img = Image.open(wall.file).convert("RGBA")
        art_img = Image.open(artwork.file).convert("RGBA")

        # Resize artwork smaller (30% of wall size)
        wall_w, wall_h = wall_img.size
        art_img = art_img.resize((wall_w // 3, wall_h // 3))

        # Paste artwork in the center
        x = wall_w // 2 - art_img.size[0] // 2
        y = wall_h // 2 - art_img.size[1] // 2
        wall_img.paste(art_img, (x, y), art_img)

        # Save preview
        filename = f"{uuid.uuid4()}.png"
        filepath = os.path.join(UPLOAD_DIR, filename)
        wall_img.save(filepath, "PNG")

        return {"preview_url": f"/{filepath}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
