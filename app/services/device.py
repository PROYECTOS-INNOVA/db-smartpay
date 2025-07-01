from fastapi import HTTPException, status
from tortoise.exceptions import IntegrityError

from app.infra.postgres.crud.device import crud_device
from app.infra.postgres.models.device import Device
from app.schemas.device import DeviceCreate, DeviceUpdate
from app.services.base import BaseService


class DeviceService(BaseService[Device, DeviceCreate, DeviceUpdate]):
    async def create(self, *, obj_in: DeviceCreate) -> Device:
        try:
            return await self.crud.create(obj_in=obj_in)
        except IntegrityError as e:
            error_message = str(e).lower()
            if (
                "duplicate key" in error_message
                or "unique constraint" in error_message
            ):
                if "device_imei_key" in error_message:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="A device with this IMEI already exists.",
                    )
            # For other integrity errors, we can be more generic
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Database integrity error: {e}",
            )


device_service = DeviceService(crud_device)
