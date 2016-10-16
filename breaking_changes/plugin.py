# TODO: the plugin should simply activate the decorator
class CollectorPlugin(object):
    def pytest_runtest_setup(self, item):
        pass


def pytest_addoption(parser):
    group = parser.getgroup(
        'collector', 'collect data while running tests'
    )


def pytest_configure(config):
    plugin = CollectorPlugin()
    if not config.pluginmanager.hasplugin('_collector'):
        config.pluginmanager.register(plugin, '_collector')
