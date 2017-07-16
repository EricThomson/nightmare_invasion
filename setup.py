from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('nightmare_invasion.py', base=base)
]

setup(name='nightmare_invasion',
      version = '0.9',
      description = 'My Little Pony twist on Space Invaders',
      options = dict(build_exe = buildOptions),
      executables = executables)
