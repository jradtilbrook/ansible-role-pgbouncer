def to_ini(databases = []):
    """
    Custom ansible filter to print out pgbouncer database connection settings
    from a list of variable objects.
    """
    s = ''
    for db in databases:
        for alias, config in db.iteritems():
            s = s + str(alias) + ' = '
            for key, value in config.iteritems():
                s = s + str(key) + '=' + str(value) + ' '
        s = s.rstrip() + '\n'
    return s

class FilterModule():
    def filters(self):
        return {'to_ini': to_ini}
