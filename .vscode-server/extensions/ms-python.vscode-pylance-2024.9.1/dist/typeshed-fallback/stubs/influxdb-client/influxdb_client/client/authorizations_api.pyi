from _typeshed import Incomplete

from influxdb_client import Authorization, Organization, User

class AuthorizationsApi:
    def __init__(self, influxdb_client) -> None: ...
    def create_authorization(
        self,
        org_id: Incomplete | None = None,
        permissions: list[Incomplete] | None = None,
        authorization: Authorization | None = None,
    ) -> Authorization: ...
    def find_authorization_by_id(self, auth_id: str) -> Authorization: ...
    def find_authorizations(self, **kwargs): ...
    def find_authorizations_by_user(self, user: User): ...
    def find_authorizations_by_user_id(self, user_id: str): ...
    def find_authorizations_by_user_name(self, user_name: str): ...
    def find_authorizations_by_org(self, org: Organization): ...
    def find_authorizations_by_org_name(self, org_name: str): ...
    def find_authorizations_by_org_id(self, org_id: str): ...
    def update_authorization(self, auth): ...
    def clone_authorization(self, auth) -> Authorization: ...
    def delete_authorization(self, auth): ...
