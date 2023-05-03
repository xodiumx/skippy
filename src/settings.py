from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str

    server_host: str
    server_port: int
    database_url: str

    jwt_secret: str
    jwt_algorithm: str
    jwt_expiration: int

    admin_username: str
    admin_password: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf8',
)
