"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ResourceName(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UUID_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SUBTYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    uuid: typing.Text
    namespace: typing.Text
    type: typing.Text
    subtype: typing.Text
    name: typing.Text

    def __init__(self, *, uuid: typing.Text=..., namespace: typing.Text=..., type: typing.Text=..., subtype: typing.Text=..., name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'namespace', b'namespace', 'subtype', b'subtype', 'type', b'type', 'uuid', b'uuid']) -> None:
        ...
global___ResourceName = ResourceName

class BoardStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class AnalogsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text

        @property
        def value(self) -> global___AnalogStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___AnalogStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...

    class DigitalInterruptsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text

        @property
        def value(self) -> global___DigitalInterruptStatus:
            ...

        def __init__(self, *, key: typing.Text=..., value: typing.Optional[global___DigitalInterruptStatus]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['key', b'key', 'value', b'value']) -> None:
            ...
    ANALOGS_FIELD_NUMBER: builtins.int
    DIGITAL_INTERRUPTS_FIELD_NUMBER: builtins.int

    @property
    def analogs(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___AnalogStatus]:
        ...

    @property
    def digital_interrupts(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___DigitalInterruptStatus]:
        ...

    def __init__(self, *, analogs: typing.Optional[typing.Mapping[typing.Text, global___AnalogStatus]]=..., digital_interrupts: typing.Optional[typing.Mapping[typing.Text, global___DigitalInterruptStatus]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['analogs', b'analogs', 'digital_interrupts', b'digital_interrupts']) -> None:
        ...
global___BoardStatus = BoardStatus

class AnalogStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    "Current value of the analog reader of a robot's board"

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___AnalogStatus = AnalogStatus

class DigitalInterruptStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int
    "Current value of the digital interrupt of a robot's board"

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___DigitalInterruptStatus = DigitalInterruptStatus

class Pose(google.protobuf.message.Message):
    """Pose is a combination of location and orientation.
    Location is expressed as distance which is represented by x , y, z coordinates. Orientation is expressed as an orientation vector which 
    is represented by o_x, o_y, o_z and theta. The o_x, o_y, o_z coordinates represent the point on the cartesian unit sphere that the end of
    the arm is pointing to (with the origin as reference). That unit vector forms an axis around which theta rotates. This means that 
    incrementing / decrementing theta will perform an inline rotation of the end effector. 
    Theta is defined as rotation between two planes: the first being defined by the origin, the point (0,0,1), and the rx, ry, rz point, and the 
    second being defined by the origin, the rx, ry, rz point and the local Z axis. Therefore, if theta is kept at zero as the north/south pole 
    is circled, the Roll will correct itself to remain in-line.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    O_X_FIELD_NUMBER: builtins.int
    O_Y_FIELD_NUMBER: builtins.int
    O_Z_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    x: builtins.float
    'millimeters from the origin'
    y: builtins.float
    'millimeters from the origin'
    z: builtins.float
    'millimeters from the origin'
    o_x: builtins.float
    'z component of a vector defining axis of rotation'
    o_y: builtins.float
    'x component of a vector defining axis of rotation'
    o_z: builtins.float
    'y component of a vector defining axis of rotation'
    theta: builtins.float
    'degrees'

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=..., o_x: builtins.float=..., o_y: builtins.float=..., o_z: builtins.float=..., theta: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['o_x', b'o_x', 'o_y', b'o_y', 'o_z', b'o_z', 'theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Pose = Pose

class PoseInFrame(google.protobuf.message.Message):
    """PoseInFrame contains a pose and the and the reference frame in which it was observed"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    reference_frame: typing.Text

    @property
    def pose(self) -> global___Pose:
        ...

    def __init__(self, *, reference_frame: typing.Text=..., pose: typing.Optional[global___Pose]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose', b'pose', 'reference_frame', b'reference_frame']) -> None:
        ...
global___PoseInFrame = PoseInFrame

class Vector3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Vector3 = Vector3

class Sphere(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RADIUS_MM_FIELD_NUMBER: builtins.int
    radius_mm: builtins.float

    def __init__(self, *, radius_mm: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['radius_mm', b'radius_mm']) -> None:
        ...
global___Sphere = Sphere

class RectangularPrism(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WIDTH_MM_FIELD_NUMBER: builtins.int
    LENGTH_MM_FIELD_NUMBER: builtins.int
    DEPTH_MM_FIELD_NUMBER: builtins.int
    width_mm: builtins.float
    length_mm: builtins.float
    depth_mm: builtins.float

    def __init__(self, *, width_mm: builtins.float=..., length_mm: builtins.float=..., depth_mm: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['depth_mm', b'depth_mm', 'length_mm', b'length_mm', 'width_mm', b'width_mm']) -> None:
        ...
global___RectangularPrism = RectangularPrism

class Geometry(google.protobuf.message.Message):
    """Geometry contains the dimensions of a given geometry and the pose of its center. The geometry is one of either a sphere or a box."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CENTER_FIELD_NUMBER: builtins.int
    SPHERE_FIELD_NUMBER: builtins.int
    BOX_FIELD_NUMBER: builtins.int

    @property
    def center(self) -> global___Pose:
        """Pose of a gemetries center point"""
        pass

    @property
    def sphere(self) -> global___Sphere:
        ...

    @property
    def box(self) -> global___RectangularPrism:
        ...

    def __init__(self, *, center: typing.Optional[global___Pose]=..., sphere: typing.Optional[global___Sphere]=..., box: typing.Optional[global___RectangularPrism]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['box', b'box', 'center', b'center', 'geometry_type', b'geometry_type', 'sphere', b'sphere']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['box', b'box', 'center', b'center', 'geometry_type', b'geometry_type', 'sphere', b'sphere']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['geometry_type', b'geometry_type']) -> typing.Optional[typing_extensions.Literal['sphere', 'box']]:
        ...
global___Geometry = Geometry

class GeometriesInFrame(google.protobuf.message.Message):
    """GeometriesinFrame contains the dimensions of a given geometry, pose of its center point, and the reference frame by which it was 
    observed.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    GEOMETRIES_FIELD_NUMBER: builtins.int
    reference_frame: typing.Text
    'Reference frame of the observer of the geometry'

    @property
    def geometries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Geometry]:
        """Dimensional type"""
        pass

    def __init__(self, *, reference_frame: typing.Text=..., geometries: typing.Optional[typing.Iterable[global___Geometry]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['geometries', b'geometries', 'reference_frame', b'reference_frame']) -> None:
        ...
global___GeometriesInFrame = GeometriesInFrame

class PointCloudObject(google.protobuf.message.Message):
    """PointCloudObject contains an image in bytes with point cloud data of all of the objects captured by a given observer as well as a 
    repeated list of geometries which respresents the center point and geometry of each of the objects within the point cloud
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POINT_CLOUD_FIELD_NUMBER: builtins.int
    GEOMETRIES_FIELD_NUMBER: builtins.int
    point_cloud: builtins.bytes
    'image frame expressed in bytes'

    @property
    def geometries(self) -> global___GeometriesInFrame:
        """volume of a given geometry"""
        pass

    def __init__(self, *, point_cloud: builtins.bytes=..., geometries: typing.Optional[global___GeometriesInFrame]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['geometries', b'geometries']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['geometries', b'geometries', 'point_cloud', b'point_cloud']) -> None:
        ...
global___PointCloudObject = PointCloudObject

class GeoPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    latitude: builtins.float
    longitude: builtins.float

    def __init__(self, *, latitude: builtins.float=..., longitude: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['latitude', b'latitude', 'longitude', b'longitude']) -> None:
        ...
global___GeoPoint = GeoPoint

class Transform(google.protobuf.message.Message):
    """Transform contains a pose and two reference frames. The first reference frame is the starting reference frame, and the second reference
    frame is the observer reference frame. The second reference frame has a pose which represents the pose of an object in the first
    reference frame as observed within the second reference frame.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFERENCE_FRAME_FIELD_NUMBER: builtins.int
    POSE_IN_OBSERVER_FRAME_FIELD_NUMBER: builtins.int
    reference_frame: typing.Text
    'the name of a given reference frame'

    @property
    def pose_in_observer_frame(self) -> global___PoseInFrame:
        """the pose of the above reference frame with respect to a different observer reference frame"""
        pass

    def __init__(self, *, reference_frame: typing.Text=..., pose_in_observer_frame: typing.Optional[global___PoseInFrame]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose_in_observer_frame', b'pose_in_observer_frame']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['pose_in_observer_frame', b'pose_in_observer_frame', 'reference_frame', b'reference_frame']) -> None:
        ...
global___Transform = Transform

class WorldState(google.protobuf.message.Message):
    """WorldState contains information about the physical environment around a given robot. All of the fields within this message are optional, 
    they can include information about the physical dimensions of an obstacle, the freespace of a robot, and any desired transforms between a
    given reference frame and a new target reference frame.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OBSTACLES_FIELD_NUMBER: builtins.int
    TRANSFORMS_FIELD_NUMBER: builtins.int

    @property
    def obstacles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GeometriesInFrame]:
        """a list of obstacles expressed as a geomtry and the reference frame in which it was observed; this field is optional"""
        pass

    @property
    def transforms(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Transform]:
        """a list of Transforms needed to transform a pose from one reference frame to another; this field is optional"""
        pass

    def __init__(self, *, obstacles: typing.Optional[typing.Iterable[global___GeometriesInFrame]]=..., transforms: typing.Optional[typing.Iterable[global___Transform]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['obstacles', b'obstacles', 'transforms', b'transforms']) -> None:
        ...
global___WorldState = WorldState