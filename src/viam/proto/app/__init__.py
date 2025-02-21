"""
@generated by Viam.
Do not edit manually!
"""
from ...gen.app.v1.app_grpc import AppServiceBase, AppServiceStub
from ...gen.app.v1.app_pb2 import (
    AddRoleRequest,
    AddRoleResponse,
    Authorization,
    AuthorizedPermissions,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
    CreateLocationRequest,
    CreateLocationResponse,
    CreateLocationSecretRequest,
    CreateLocationSecretResponse,
    CreateModuleRequest,
    CreateModuleResponse,
    CreateOrganizationInviteRequest,
    CreateOrganizationInviteResponse,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteFragmentRequest,
    DeleteFragmentResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    DeleteLocationSecretRequest,
    DeleteLocationSecretResponse,
    DeleteOrganizationInviteRequest,
    DeleteOrganizationInviteResponse,
    DeleteOrganizationMemberRequest,
    DeleteOrganizationMemberResponse,
    DeleteOrganizationRequest,
    DeleteOrganizationResponse,
    DeleteRobotPartRequest,
    DeleteRobotPartResponse,
    DeleteRobotPartSecretRequest,
    DeleteRobotPartSecretResponse,
    DeleteRobotRequest,
    DeleteRobotResponse,
    Fragment,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationNamespaceAvailabilityRequest,
    GetOrganizationNamespaceAvailabilityResponse,
    GetOrganizationRequest,
    GetOrganizationResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotRequest,
    GetRobotResponse,
    GetRoverRentalRobotsRequest,
    GetRoverRentalRobotsResponse,
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListModulesRequest,
    ListModulesResponse,
    ListOrganizationMembersRequest,
    ListOrganizationMembersResponse,
    ListOrganizationsByUserRequest,
    ListOrganizationsByUserResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LocationAuth,
    LocationAuthRequest,
    LocationAuthResponse,
    LocationOrganization,
    LogEntry,
    MarkPartAsMainRequest,
    MarkPartAsMainResponse,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    Model,
    Module,
    ModuleFileInfo,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    OrganizationInvite,
    OrganizationMember,
    OrgDetails,
    RemoveRoleRequest,
    RemoveRoleResponse,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
    RobotPart,
    RobotPartHistoryEntry,
    RoverRentalRobot,
    SharedSecret,
    ShareLocationRequest,
    ShareLocationResponse,
    StorageConfig,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    UnshareLocationRequest,
    UnshareLocationResponse,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    UploadModuleFileResponse,
    Uploads,
    VersionHistory,
    Visibility,
)

__all__ = [
    "AppServiceBase",
    "AppServiceStub",
    "AddRoleRequest",
    "AddRoleResponse",
    "Authorization",
    "AuthorizedPermissions",
    "CheckPermissionsRequest",
    "CheckPermissionsResponse",
    "CreateFragmentRequest",
    "CreateFragmentResponse",
    "CreateLocationRequest",
    "CreateLocationResponse",
    "CreateLocationSecretRequest",
    "CreateLocationSecretResponse",
    "CreateModuleRequest",
    "CreateModuleResponse",
    "CreateOrganizationInviteRequest",
    "CreateOrganizationInviteResponse",
    "CreateOrganizationRequest",
    "CreateOrganizationResponse",
    "CreateRobotPartSecretRequest",
    "CreateRobotPartSecretResponse",
    "DeleteFragmentRequest",
    "DeleteFragmentResponse",
    "DeleteLocationRequest",
    "DeleteLocationResponse",
    "DeleteLocationSecretRequest",
    "DeleteLocationSecretResponse",
    "DeleteOrganizationInviteRequest",
    "DeleteOrganizationInviteResponse",
    "DeleteOrganizationMemberRequest",
    "DeleteOrganizationMemberResponse",
    "DeleteOrganizationRequest",
    "DeleteOrganizationResponse",
    "DeleteRobotPartRequest",
    "DeleteRobotPartResponse",
    "DeleteRobotPartSecretRequest",
    "DeleteRobotPartSecretResponse",
    "DeleteRobotRequest",
    "DeleteRobotResponse",
    "Fragment",
    "GetFragmentRequest",
    "GetFragmentResponse",
    "GetLocationRequest",
    "GetLocationResponse",
    "GetModuleRequest",
    "GetModuleResponse",
    "GetOrganizationNamespaceAvailabilityRequest",
    "GetOrganizationNamespaceAvailabilityResponse",
    "GetOrganizationRequest",
    "GetOrganizationResponse",
    "GetRobotPartHistoryRequest",
    "GetRobotPartHistoryResponse",
    "GetRobotPartLogsRequest",
    "GetRobotPartLogsResponse",
    "GetRobotPartRequest",
    "GetRobotPartResponse",
    "GetRobotPartsRequest",
    "GetRobotPartsResponse",
    "GetRobotRequest",
    "GetRobotResponse",
    "GetRoverRentalRobotsRequest",
    "GetRoverRentalRobotsResponse",
    "GetUserIDByEmailRequest",
    "GetUserIDByEmailResponse",
    "ListAuthorizationsRequest",
    "ListAuthorizationsResponse",
    "ListFragmentsRequest",
    "ListFragmentsResponse",
    "ListLocationsRequest",
    "ListLocationsResponse",
    "ListModulesRequest",
    "ListModulesResponse",
    "ListOrganizationMembersRequest",
    "ListOrganizationMembersResponse",
    "ListOrganizationsByUserRequest",
    "ListOrganizationsByUserResponse",
    "ListOrganizationsRequest",
    "ListOrganizationsResponse",
    "ListRobotsRequest",
    "ListRobotsResponse",
    "Location",
    "LocationAuth",
    "LocationAuthRequest",
    "LocationAuthResponse",
    "LocationOrganization",
    "LogEntry",
    "MarkPartAsMainRequest",
    "MarkPartAsMainResponse",
    "MarkPartForRestartRequest",
    "MarkPartForRestartResponse",
    "Model",
    "Module",
    "ModuleFileInfo",
    "NewRobotPartRequest",
    "NewRobotPartResponse",
    "NewRobotRequest",
    "NewRobotResponse",
    "OrgDetails",
    "Organization",
    "OrganizationInvite",
    "OrganizationMember",
    "RemoveRoleRequest",
    "RemoveRoleResponse",
    "ResendOrganizationInviteRequest",
    "ResendOrganizationInviteResponse",
    "Robot",
    "RobotPart",
    "RobotPartHistoryEntry",
    "RoverRentalRobot",
    "ShareLocationRequest",
    "ShareLocationResponse",
    "SharedSecret",
    "StorageConfig",
    "TailRobotPartLogsRequest",
    "TailRobotPartLogsResponse",
    "UnshareLocationRequest",
    "UnshareLocationResponse",
    "UpdateFragmentRequest",
    "UpdateFragmentResponse",
    "UpdateLocationRequest",
    "UpdateLocationResponse",
    "UpdateModuleRequest",
    "UpdateModuleResponse",
    "UpdateOrganizationInviteAuthorizationsRequest",
    "UpdateOrganizationInviteAuthorizationsResponse",
    "UpdateOrganizationRequest",
    "UpdateOrganizationResponse",
    "UpdateRobotPartRequest",
    "UpdateRobotPartResponse",
    "UpdateRobotRequest",
    "UpdateRobotResponse",
    "UploadModuleFileRequest",
    "UploadModuleFileResponse",
    "Uploads",
    "VersionHistory",
    "Visibility",
]
