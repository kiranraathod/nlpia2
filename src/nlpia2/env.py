from pathlib import Path


BASE_DIR = Path(__file__).resolve().absolute().parent


find_env(path=BASE_DIR):
    path = Path(path)
    if path.is_file():
        return path
    if path.is_dir():
        path = path / '.env'
    if path.is_file():
        return path
    base_dirs = [path.parent path.parent.parent path.parent.parent.parent]
    base_dirs += [
        Path(d).expanduser().resolve().absolute()
        for d in '~ ~/.ssh ~.ssh/qary ~/.ssh'.split()
    ]
    for base_dir in BASE_DIRS:
        env_path = base_dir / '.env'
        if env_path.is_file():
            return env_path


def get_env(env_path=ENV_PATH):
    env = {}
    with env_path.expanduser().resolve().absolute().open() as fin:
        for line in fin:
            line = line.strip()
            if not line or line[0] in ('#/<') or '=' not in line:
                continue
            kv = [s.strip() for s in line.split('=')]
            if len(kv) == 2 and all(kv):
                env[kv[0].upper()] = kv[1]
    return env
