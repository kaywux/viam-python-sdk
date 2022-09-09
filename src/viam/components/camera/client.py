from io import BytesIO
from typing import Any, Dict, Tuple, Union

from grpclib.client import Channel
from PIL import Image
from viam.components.generic.client import do_command
from viam.components.types import CameraMimeType, RawImage
from viam.proto.api.component.camera import (
    CameraServiceStub,
    GetFrameRequest,
    GetFrameResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    IntrinsicParameters,
)

from .camera import Camera


class CameraClient(Camera):
    """
    gRPC client for the Camera component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = CameraServiceStub(channel)
        super().__init__(name)

    async def get_frame(self, mime_type: str = CameraMimeType.PNG) -> Union[Image.Image, RawImage]:
        request = GetFrameRequest(name=self.name, mime_type=mime_type)
        response: GetFrameResponse = await self.client.GetFrame(request)
        try:
            mimetype = CameraMimeType(response.mime_type)
            if mimetype == CameraMimeType.RAW:
                raise ValueError("Raw mime type should go return a RawImage")
        except ValueError:
            # If the mime type is raw or unknown, return a RawImage
            image = RawImage(response.image, response.mime_type, response.width_px, response.height_px)
            return image

        return Image.open(BytesIO(response.image), formats=["JPEG", "PNG"])

    async def get_point_cloud(self) -> Tuple[bytes, str]:
        request = GetPointCloudRequest(name=self.name, mime_type=CameraMimeType.PCD)
        response: GetPointCloudResponse = await self.client.GetPointCloud(request)
        return (response.point_cloud, response.mime_type)

    async def get_properties(self) -> IntrinsicParameters:
        response: GetPropertiesResponse = await self.client.GetProperties(GetPropertiesRequest(name=self.name))
        return response.intrinsic_parameters

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
