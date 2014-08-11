from ConfigParser import ConfigParser
from sqlalchemy.engine.url import URL
from ast import literal_eval


def parse(cell, config, user_ns={}):
    parts = [part.strip() for part in cell.split(None, 1)]
    if not parts:
        return {'connection': '', 'sql': ''}
    if parts[0].startswith('[') and parts[0].endswith(']'):
        part0 = parts[0].lstrip('[').rstrip(']').split(',')
        section = part0[0]
        var_names = part0[1:]
        parser = ConfigParser()
        parser.read(config.dsn_filename)
        cfg_dict = dict(parser.items(section))
        if 'query' in cfg_dict.keys():
            cfg_dict['query'] = literal_eval(cfg_dict['query'])

        # TODO currently the url has to be turned into a string object
        # so that the Connection object can find it in its dictionary
        connection = str(URL(**cfg_dict))
        sql = parts[1].strip() if len(parts) > 1 else ''
        for var_name in var_names or []:
            var_name = var_name.strip()
            var_val = user_ns.get(var_name)
            if var_val:
                sql = sql.replace(':{}'.format(var_name), str(var_val))
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
