class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/pybank"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "meu_segredo"
