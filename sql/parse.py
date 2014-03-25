from ConfigParser import ConfigParser
from sqlalchemy.engine.url import URL
from ast import literal_eval


def parse(cell, config):
    parts = [part.strip() for part in cell.split(None, 1)]
    if not parts:
        return {'connection': '', 'sql': ''}
    if parts[0].startswith('[') and parts[0].endswith(']'):
        section = parts[0].lstrip('[').rstrip(']')
        parser = ConfigParser()
        parser.read(config.dsn_filename)
        cfg_dict = dict(parser.items(section))
        if 'query' in cfg_dict.keys():
            cfg_dict['query'] = literal_eval(cfg_dict['query'])

        connection = URL(**cfg_dict)
        sql = parts[1].strip() if len(parts) > 1 else ''
    elif '@' in parts[0] or '://' in parts[0]:
        connection = parts[0].strip()
        if len(parts) > 1:
            sql = parts[1].strip()
        else:
            sql = ''
    else:
        connection = ''
        sql = cell.strip()
    return {'connection': connection,
            'sql': sql}
