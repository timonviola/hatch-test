1. `hatch run test:test` fails with ModuleNotFoundError
2. run `hatch env remove test` and `hatch clean`, add checkout the previous commit (toml is without onbuild table)
3. run tests again, they should pass

Thank you for checking!
