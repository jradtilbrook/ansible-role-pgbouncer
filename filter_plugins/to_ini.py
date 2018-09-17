def to_ini(databases = []):
    """
    Custom ansible filter to print out pgbouncer database connection settings
    from a list of variable objects.
    """
    s = ''
    for db in databases:
        for alias, config in db.items():
            s = s + str(alias) + ' = '
            for key, value in config.items():
                s = s + str(key) + '=' + str(value) + ' '
        s = s.rstrip() + '\n'
    return s.rstrip()

class FilterModule():
    def filters(self):
        return {'pgbouncer_to_ini': to_ini}
