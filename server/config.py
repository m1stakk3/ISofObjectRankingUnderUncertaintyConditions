import os
from dataclasses import dataclass


@dataclass
class Config:
    ip: str = "0.0.0.0"
    port: int = 8999
    secret_key: bytes = os.urandom(10)
