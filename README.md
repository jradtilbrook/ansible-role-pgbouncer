# Ansible Role: PgBouncer [![Build Status](https://travis-ci.org/jradtilbrook/ansible-role-pgbouncer.svg?branch=master)](https://travis-ci.org/jradtilbrook/ansible-role-pgbouncer)

This role installs and configures the PgBouncer connection pooler for
PostgreSQL.

It has only been designed to work on Ubuntu 16.04, but other Debian flavours
should also work.


## Requirements

None.


## Role Variables

The `pgbouncer_databases` array allows a very dynamic database setup. Any
property allowed in the connection string can be defined under this array and
will automatically be added to the alias definition. The example below
configures a `dev` database alias that pools connections to the `postgres`
database on `postgres:5432` connecting as `foo:md5asdofiasodfa09f9832f`. You can
define more databases in the same fashion.

```yaml
pgbouncer_databases:
  - dev:
      host: postgres # or the actual ip address
      port: 5432
      dbname: postgres
      user: foo
      password: md5asdofiasodfa09f9832f
```

This role can also optionally install the `postgresql-client` package for
command-line access to PostgreSQL or PgBouncer. To install this package set
`pgbouncer_install_psql: true`.

The configuration template allows some values to be overridden. To achieve this,
create a variable named after the configuration property you want to change and
prefix it with `pgbouncer_`. For example, to override the default `listen_port`
of 6432, pass a variable named `pgbouncer_listen_port`.  See the template file
for other configs that can be overridden this way. Note that not all settings
are available, only some common ones that I use.

**Note:** Some variables expect an array - it should be obvious which ones.

See the [`defaults/main.yml`](defaults/main.yml) for more descriptions of other
variables. You should also check
[`templates/pgbouncer.ini.j2`](templates/pgbouncer.ini.j2) for possible extra
variables you can set.


## Resources

Documentation related to PgBouncer can be found at the links below:

- [documentation](https://pgbouncer.github.io/)
- [github repository](https://github.com/pgbouncer/pgbouncer)


## Dependencies

None.


## Example Playbook

```yaml
- hosts: servers
  become: yes

  roles:
    - role: jradtilbrook.pgbouncer
      pgbouncer_databases:
        - testing:
            host: postgres
            port: 5432
            dbname: postgres
```


## License

MIT
