"""Initialize Flask app."""

import os

from flask import Flask

import AditiFlix_App.adapters.movie_repository as repo
from AditiFlix_App.adapters import database_repository
from AditiFlix_App.adapters.memory_repository import MemoryRepository, populate
from AditiFlix_App.adapters.orm import metadata, map_model_to_tables

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('AditiFlix_App', 'adapters', 'datafiles')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    if app.config['REPOSITORY'] == 'memory':
        # Create the MemoryRepository instance for a memory-based repository.
        repo.repo_instance = MemoryRepository()
        populate(data_path, repo.repo_instance, 'Data13Movies.csv')

    if app.config['REPOSITORY'] == 'database':
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']
        database_echo = app.config['SQLALCHEMY_ECHO']
        database_engine = create_engine(database_uri,
                                        connect_args={"check_same_thread": False},
                                        poolclass=NullPool,
                                        echo=database_echo)

        clear_mappers()
        map_model_to_tables()
        metadata.create_all(database_engine)
        # Create the database session factory using sessionmaker (this has to be done once, in a global manner)
        session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
        repo.repo_instance = database_repository.SqlAlchemyRepository(session_factory)
        database_repository.populate(database_engine, 'Data13Movies.csv')

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)
        from .auth import auth
        app.register_blueprint(auth.authentication_blueprint)
        from .users import user
        app.register_blueprint(user.user_blueprint)
        from .movies import movie
        app.register_blueprint(movie.movie_blueprint)
        from .reviews import review
        app.register_blueprint(review.review_blueprint)
    return app
