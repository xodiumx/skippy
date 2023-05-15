from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    user_secret_key: str

    server_host: str
    server_port: int
    
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str

    jwt_secret: str
    jwt_algorithm: str
    jwt_expiration: int

    admin_username: str
    admin_password: str


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf8',
)
