import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


def init_db():
    db.create_all()
    u=User(email="ameerhamza0220@gmail.com",username='AmeerHamza',password='1234')
    db.session.add(u)
    db.session.commit()
    # # Create a test user
    # new_user = User('a@a.com', 'aaaaaaaa')
    # new_user.display_name = 'Nathan'
    # db.session.add(new_user)
    # db.session.commit()
    #
    # new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
    # db.session.commit()


if __name__ == '__main__':
    init_db()