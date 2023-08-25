#### finder
An object that tries to find the loader for a module that is being imported.

Since Python 3.3, there are two types of finder: meta path finders for use with
`sys.meta_path`, and path entry finders for use with `sys.path_hooks`.

See PEP 302, PEP 420 and PEP 451 for much more detail.

#### importing
The process by which Python code in one module is made available to Python code in another module.

#### importer
An object that both finds and loads a module; both a finder and loader object.

#### loader
An object that loads a module. It must define a method named load_module().
A loader is typically returned by a finder. See PEP 302 for details and `importlib.abc.Loader`
for an abstract base class.

#### module
An object that serves as an organizational unit of Python code.
Modules have a namespace containing arbitrary Python objects.
Modules are loaded into Python by the process of importing.

#### namespace package
A PEP 420 package which serves only as a container for subpackages.
Namespace packages may have no physical representation,
and specifically are not like a regular package because they have no `__init__.py` file.

#### package
A Python module which can contain submodules or recursively, subpackages.

Technically, a package is a Python module with a `__path__` attribute.

See also regular package and namespace package.

#### regular package
A traditional package, such as a directory containing an `__init__.py` file.
