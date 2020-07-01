import yaml


def get_intranet_configuration():
    with open('configuration.yml', 'r') as stream:
        conf = yaml.safe_load(stream)

        intranet = conf['intranet']
        email = intranet['email']
        password = intranet['password']
        intranet_url = intranet['base_url']

    return email, password, intranet_url
