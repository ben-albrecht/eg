# Input/Output library
C++ includes two input/output libraries: a modern, stream-based I/O library and
the standard set of C-style I/O functions.

## Stream-based I/O
The stream-based input/output library is organized around abstract input/output devices.
These abstract devices allow the same code to handle input/output to files, memory
streams, or custom adaptor devices that perform arbitrary operations (e.g.
compression) on the fly.

Most of the classes are templated, so they can be
adapted to any basic character type. Separate typedefs are provided for the
most common basic character types (char and wchar_t). The classes are organized
into the following hierarchy:

![alt tag](https://github.com/exit-1/eg/tree/master/cpp/Concepts/IO/std-io-complete-inheritance.svg)

(cppreference.com/w/cpp/io)


