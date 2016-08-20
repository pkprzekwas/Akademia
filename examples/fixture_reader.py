import csv
import os


class FixtureReader:
    def __init__(self, fixtures_path='fixtures'):
        self._path = fixtures_path

    def _read_fixtures(self, file_name):
        file_path = os.path.join(os.getcwd(), self._path, file_name)
        fixtures_data = {}
        with open(file_path) as f:
            fixtures = csv.DictReader(f)
            for fixture in fixtures:
                fixture_name = fixture.pop('fixture_name')
                fixtures_data[fixture_name] = fixture
        return fixtures_data

    def get_fixture(self, file_name, fixture_name):
        file_name += '.csv'
        fixtures = self._read_fixtures(file_name)
        return fixtures.get(fixture_name)
